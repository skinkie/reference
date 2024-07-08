import datetime
import glob
from typing import List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

import lxml
import hashlib

from callsprofile import CallsProfile
from dbaccess import load_local, load_generator
from gtfsprofile import GtfsProfile
from netex import Line, StopPlace, Codespace, ScheduledStopPoint, LocationStructure2, PassengerStopAssignment, \
    Authority, Operator, Branding, UicOperatingPeriod, DayTypeAssignment, ServiceJourney, ServiceJourneyPattern, \
    DataSource, StopPlaceEntrance
from nordicprofile import NordicProfile
from refs import getId, getRef, getIndex

import duckdb as sqlite3

from decimal import Decimal

from timetabledpassingtimesprofile import TimetablePassingTimesProfile

import csv

import zipfile


def convert(archive, database: str):
    agencies = {}
    used_agencies = set([])
    routes = {}
    stops = {}
    psas = {}
    uic_operating_periods = {}
    max_date = datetime.date.today()
    calendar_dates = {}

    # We can't append in a ZipFile
    # GtfsProfile.writeToZipFile(archive, 'trips.txt', [GtfsProfile.empty_trip], write_header=True)
    # GtfsProfile.writeToZipFile(archive, 'stop_times.txt', [GtfsProfile.empty_stop_time], write_header=True)

    with sqlite3.connect(database) as con:
        datasources: List[DataSource] = load_local(con, DataSource, 1)
        codespaces: List[Codespace] = load_local(con, Codespace, 1)

        for authority in load_generator(con, Authority):
            agency = GtfsProfile.projectAuthorityToAgency(authority)
            agencies[agency['agency_id']] = agency

        for operator in load_generator(con, Operator):
            agency = GtfsProfile.projectOperatorToAgency(operator)
            agencies[agency['agency_id']] = agency

        stop_places = getIndex(load_local(con, StopPlace))
        quay_to_sp = {}
        for stop_place in stop_places.values():
            stop_place: StopPlace
            for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                quay_to_sp[quay.id] = stop_place

        psas = {}
        for psa in load_generator(con, PassengerStopAssignment):
            psa: PassengerStopAssignment
            if psa.taxi_rank_ref_or_stop_place_ref_or_stop_place is not None:
                psas[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = stop_places[psa.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref]
            elif psa.taxi_stand_ref_or_quay_ref_or_quay is not None:
                psas[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = quay_to_sp[psa.taxi_stand_ref_or_quay_ref_or_quay.ref]

        # TODO: GTFS does not support Branding, so in order to facilitate it we will make it a separate Agency
        # A branding must have an 'original' agency or authority
        # for branding in load_generator(con, Branding):
        #     agency = GtfsProfile.projectBrandingToAgency(branding)
        #     agencies[agency['agency_id']] = agency

        for scheduled_stop_point in load_local(con, ScheduledStopPoint):
            stop_place = psas.get(scheduled_stop_point.id, None)
            stop_place_ref = getRef(stop_place)
            stop = GtfsProfile.projectScheduledStopPointToStop(scheduled_stop_point, stop_place_ref)
            if stop is not None:
                stops[stop['stop_id']] = stop
                if stop_place is not None:
                    if stop_place.entrances is not None:
                        for entrance in stop_place.entrances.parking_entrance_ref_or_entrance_ref_or_entrance:
                            if isinstance(entrance, StopPlaceEntrance):
                                stop = GtfsProfile.projectStopEntranceToStop(entrance, stop_place_ref)
                                if stop is not None:
                                    stops[stop['stop_id']] = stop

        for line in load_generator(con, Line):
            route = GtfsProfile.projectLineToRoute(line)
            routes[route['route_id']] = route
            used_agencies.add(route['agency_id'])

        trips = []
        stop_times = []
        service_journey_patterns = load_local(con, ServiceJourneyPattern)

        service_journey_patterns_index = getIndex(service_journey_patterns)

        for service_journey in load_generator(con, ServiceJourney):
            service_journey_pattern = service_journey_patterns_index.get(service_journey.journey_pattern_ref.ref) if service_journey.journey_pattern_ref else None
            trip = GtfsProfile.projectServiceJourneyToTrip(service_journey, service_journey_pattern)
            trips.append(trip)

            CallsProfile.getCallsFromTimetabledPassingTimes(service_journey, service_journey_pattern)
            stop_times += list(GtfsProfile.projectServiceJourneyToStopTimes(service_journey))

        # TODO: maybe do this per trip?
        GtfsProfile.writeToZipFile(archive,'trips.txt', trips, write_header=True)
        GtfsProfile.writeToZipFile(archive,'stop_times.txt', stop_times, write_header=True)

        GtfsProfile.writeToZipFile(archive,'routes.txt', list(routes.values()), write_header=True)
        GtfsProfile.writeToZipFile(archive,'agency.txt', [y for x, y in agencies.items() if x in used_agencies], write_header=True)
        GtfsProfile.writeToZipFile(archive,'stops.txt', list(stops.values()), write_header=True)
        GtfsProfile.writeToZipFile(archive,'calendar_dates.txt', [item for row in calendar_dates.values() for item in row], write_header=True)

        GtfsProfile.writeToZipFile(archive,'feed_info.txt', [{
            'feed_publisher_name': datasources[0].name.value if len(datasources) > 0 else 'Publication Delivery',
            'feed_publisher_url': codespaces[0].xmlns_url if len(codespaces) > 0 else 'http://publicationdelivery.eu',
            'feed_lang': 'en', # TODO
            'default_lang': 'en', # TODO
            'feed_start_date': str(datetime.date.today()).replace('-', ''),
            'feed_end_date': str(max_date).replace('-', ''),
            'feed_version': str(datetime.date.today()).replace('-', ''),
            'feed_contact_email': '',
            'feed_contact_url': ''
        }], write_header=True)


if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Convert prepared DuckDB database into GTFS')
    argument_parser.add_argument('netex', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('gtfs', type=str, help='The DuckDB to be overwritten with the NeTEx context')
    args = argument_parser.parse_args()

    with zipfile.ZipFile(args.gtfs, 'w') as archive:
        convert(archive, args.netex)
