import datetime
import glob
import re
from typing import List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

import lxml
import hashlib

from callsprofile import CallsProfile
from netexio.database import Database
from netexio.dbaccess import load_local, load_generator
from gtfsprofile import GtfsProfile
from netex import Line, StopPlace, Codespace, ScheduledStopPoint, LocationStructure2, PassengerStopAssignment, \
    Authority, Operator, Branding, UicOperatingPeriod, DayTypeAssignment, ServiceJourney, ServiceJourneyPattern, \
    DataSource, StopPlaceEntrance, TemplateServiceJourney, InterchangeRule, ServiceJourneyInterchange, JourneyMeeting, \
    AvailabilityCondition
from nordicprofile import NordicProfile
from refs import getId, getRef, getIndex

from decimal import Decimal

from timetabledpassingtimesprofile import TimetablePassingTimesProfile

import csv

import zipfile
from aux_logging import *
import traceback
from configuration import defaults
def convert(archive, database: str):
    agencies = {}
    used_agencies = set([])
    routes = {}
    stops = {}
    psas = {}
    uic_operating_periods = {}
    max_date = datetime.date.today()
    calendars = {}
    calendar_dates = {}

    # We can't append in a ZipFile
    # GtfsProfile.writeToZipFile(archive, 'trips.txt', [GtfsProfile.empty_trip], write_header=True)
    # GtfsProfile.writeToZipFile(archive, 'stop_times.txt', [GtfsProfile.empty_stop_time], write_header=True)

    with Database(database) as db_read:
        datasources: List[DataSource] = load_local(db_read, DataSource, 1)
        codespaces: List[Codespace] = load_local(db_read, Codespace, 1)

        for authority in load_generator(db_read, Authority):
            agency = GtfsProfile.projectAuthorityToAgency(authority)
            agencies[agency['agency_id']] = agency

        for operator in load_generator(db_read, Operator):
            agency = GtfsProfile.projectOperatorToAgency(operator)
            agencies[agency['agency_id']] = agency

        stop_places = getIndex(load_local(db_read, StopPlace))
        quay_to_sp = {}
        for stop_place in stop_places.values():
            stop_place: StopPlace
            if stop_place.quays:
                for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    # TODO: Replace with proper checks based on object type.
                    if hasattr(quay,"id"):
                        quay_to_sp[quay.id] = stop_place
                    else:
                        quay_to_sp[quay.ref] = stop_place

        psas = {}
        for psa in load_generator(db_read, PassengerStopAssignment):
            psa: PassengerStopAssignment
            if psa.taxi_rank_ref_or_stop_place_ref_or_stop_place is not None:
                sp = stop_places.get(psa.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref, None)
                if sp is not None:
                    psas[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = sp
            elif psa.taxi_stand_ref_or_quay_ref_or_quay is not None:
                sp = quay_to_sp.get(psa.taxi_stand_ref_or_quay_ref_or_quay.ref, None)
                if sp is not None:
                    psas[psa.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = sp

        # TODO: GTFS does not support Branding, so in order to facilitate it we will make it a separate Agency
        # A branding must have an 'original' agency or authority
        # for branding in load_generator(db_read, Branding):
        #     agency = GtfsProfile.projectBrandingToAgency(branding)
        #     agencies[agency['agency_id']] = agency

        for scheduled_stop_point in load_local(db_read, ScheduledStopPoint):
            stop_place = psas.get(scheduled_stop_point.id, None)
            if stop_place is not None:
                stop_place_ref = getRef(stop_place)
                stop = GtfsProfile.projectStopPlaceToStop(stop_place)
                stops[stop['stop_id']] = stop
            else:
                stop_place_ref = None

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

        for line in load_generator(db_read, Line):
            route = GtfsProfile.projectLineToRoute(line)
            if route is not None:
                routes[route['route_id']] = route
                used_agencies.add(route['agency_id'])

        trips = []
        stop_times = []
        service_journey_patterns = load_local(db_read, ServiceJourneyPattern)

        service_journey_patterns_index = getIndex(service_journey_patterns)

        for service_journey in load_generator(db_read, ServiceJourney):
            service_journey_pattern = service_journey_patterns_index.get(service_journey.journey_pattern_ref.ref) if service_journey.journey_pattern_ref else None
            trip = GtfsProfile.projectServiceJourneyToTrip(service_journey, service_journey_pattern)
            trips.append(trip)

            CallsProfile.getCallsFromTimetabledPassingTimes(service_journey, service_journey_pattern)
            stop_times += list(GtfsProfile.projectServiceJourneyToStopTimes(service_journey))

        frequencies = []
        for template_service_journey in load_generator(db_read, TemplateServiceJourney):
            service_journey_pattern = service_journey_patterns_index.get(template_service_journey.journey_pattern_ref.ref) if template_service_journey.journey_pattern_ref else None
            trip = GtfsProfile.projectServiceJourneyToTrip(template_service_journey, service_journey_pattern)
            trips.append(trip)

            CallsProfile.getCallsFromTimetabledPassingTimes(service_journey, service_journey_pattern)
            stop_times += list(GtfsProfile.projectServiceJourneyToStopTimes(service_journey))

            frequencies += list(GtfsProfile.projectTemplateServiceJourneyToFrequency(template_service_journey))

        # TODO: maybe do this per trip?
        GtfsProfile.writeToZipFile(archive,'trips.txt', trips, write_header=True)
        if len(frequencies) > 0:
            GtfsProfile.writeToZipFile(archive, 'frequencies.txt', frequencies, write_header=True)

        GtfsProfile.writeToZipFile(archive,'stop_times.txt', stop_times, write_header=True)
        trips = frequencies = stop_times = None

        GtfsProfile.writeToZipFile(archive,'routes.txt', list(routes.values()), write_header=True)
        GtfsProfile.writeToZipFile(archive,'agency.txt', [y for x, y in agencies.items() if x in used_agencies], write_header=True)
        GtfsProfile.writeToZipFile(archive,'stops.txt', list(stops.values()), write_header=True)
        routes = agency = stops = None

        # TODO: this all asumes that we take a specific type. GTFS handles it differently.
        for uic_operating_period in load_generator(db_read, UicOperatingPeriod):
            operational_dates = NordicProfile.getOperationalDates(uic_operating_period)
            if operational_dates[-1] > max_date:
                max_date = operational_dates[-1]
            uic_operating_periods[uic_operating_period.id] = operational_dates

        for day_type_assignment in load_generator(db_read, DayTypeAssignment):
            calendar_dates[day_type_assignment.day_type_ref.ref] = list(
                GtfsProfile.getCalendarDates(day_type_assignment.day_type_ref.ref,
                                             uic_operating_periods[day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date.ref]))

        # This is what we produce ourselves, it splits the exceptions in positive and negative values, and a separate availability condition for the 'calendar'.
        for availibility_condition in load_generator(db_read, AvailabilityCondition):
            # TODO: This is a hack. See #136
            service_id = re.sub('_[12]$', '', availibility_condition.id)
            combined = list(GtfsProfile.getCalendarAndCalendarDates(service_id, availibility_condition))
            exceptions = []
            for calendar, calendar_date in combined:
                if calendar is not None:
                    calendars[service_id] = calendar

                if calendar_date is not None:
                    exceptions.append(calendar_date)

            l = calendar_dates.get(service_id, [])
            calendar_dates[service_id] = l + exceptions

        if len(calendars.values()) > 0:
            GtfsProfile.writeToZipFile(archive, 'calendar.txt', list(calendars.values()), write_header=True)

        GtfsProfile.writeToZipFile(archive,'calendar_dates.txt', [item for row in calendar_dates.values() for item in row], write_header=True)

        transfers = [GtfsProfile.projectInterchangeRuleToTransfer(transfer) for transfer in load_generator(db_read, InterchangeRule)] + [GtfsProfile.projectServiceJourneyInterchangeToTransfer(transfer) for transfer in load_generator(db_read, ServiceJourneyInterchange)] + [GtfsProfile.projectServiceJourneyMeeting(transfer) for transfer in load_generator(db_read, JourneyMeeting)]

        transfers = list({(v['from_stop_id'], v['to_stop_id'], v['from_route_id'], v['to_route_id'], v['from_trip_id'], v['to_trip_id'], v['transfer_type'], v['min_transfer_time']):v for v in transfers}.values())

        GtfsProfile.writeToZipFile(archive, 'transfers.txt', transfers, write_header=True)

        GtfsProfile.writeToZipFile(archive,'feed_info.txt', [{
            'feed_publisher_name': datasources[0].name.value if len(datasources) > 0 else defaults["feed_publisher_name"],
            'feed_publisher_url': codespaces[0].xmlns_url if len(codespaces) > 0 else defaults["feed_publisher_url"],
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
    argument_parser.add_argument('--log_file', type=str, required=False, help='the logfile')
    args = argument_parser.parse_args()
    mylogger = prepare_logger(logging.INFO, args.log_file)

    try:
        with zipfile.ZipFile(args.gtfs, 'w') as archive:
            convert(archive, args.netex)
    except Exception as e:
        log_all(logging.ERROR,f'{e}',traceback.format_exc())