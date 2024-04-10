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
from gtfsprofile import GtfsProfile
from netex import Line, StopPlace, Codespace, ScheduledStopPoint, LocationStructure2, PassengerStopAssignment, \
    Authority, Operator, Branding, UicOperatingPeriod, DayTypeAssignment, ServiceJourney, ServiceJourneyPattern
from nordicprofile import NordicProfile
from refs import getId, getRef, getIndex

from decimal import Decimal

def get_location_hash(location: LocationStructure2, digits=5):
    return str(location.latitude)[0:5] + '_' + str(location.longitude)[0:5]

def check_national_grid00(location: LocationStructure2):
    if location is None:
        return True
    return str(location.latitude)[0:6] == '48.930' and str(location.longitude)[0:6] == '5.0770'

import csv

def convert():
    stations = {}
    with open('/home/skinkie/Sources/stations/stations.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if row['latitude'] != '':
                # stations[row['uic']] = LocationStructure2(latitude=Decimal(row['latitude']), longitude=Decimal(row['longitude']))
                stations[row['db_id']] = LocationStructure2(latitude=Decimal(row['latitude']), longitude=Decimal(row['longitude']))


    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    codespace: Codespace = Codespace(id="LU", xmlns="LU")

    agencies = {}
    used_agencies = set([])
    routes = {}
    stops = {}
    psas = {}
    uic_operating_periods = {}
    max_date = datetime.date.today()
    calendar_dates = {}

    GtfsProfile.writeToFile('/tmp/trips.txt', [GtfsProfile.empty_trip], write_header=True)
    GtfsProfile.writeToFile('/tmp/stop_times.txt', [GtfsProfile.empty_stop_time], write_header=True)

    for input_filename in glob.glob("/tmp/lux/*/*.xml"):
        tree = lxml.etree.parse(input_filename)

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Authority"):
            authority: Authority = parser.parse(element, Authority)
            agency = GtfsProfile.projectAuthorityToAgency(authority)
            agencies[agency['agency_id']] = agency

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Operator"):
            operator: Operator = parser.parse(element, Operator)
            agency = GtfsProfile.projectOperatorToAgency(operator)
            agencies[agency['agency_id']] = agency

        # TODO: GTFS does not support Branding, so in order to facilitate it we will make it a separate Agency
        # A branding must have an 'original' agency or authority
        # for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Branding"):
        #    branding: Branding = parser.parse(element, branding)
        #    agency = GtfsProfile.projectBrandingToAgency(branding)
        #    agencies[agency['agency_id']] = agency

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Line"):
            line: Line = parser.parse(element, Line)
            route = GtfsProfile.projectLineToRoute(line)
            routes[route['route_id']] = route
            used_agencies.add(route['agency_id'])

        stop_place_hash = {}
        stop_place_name = {}
        stop_place_id = {}
        quay_to_sp = {}

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}StopPlace"):
            stop_place: StopPlace = parser.parse(element, StopPlace)

            # Lux hack, the IVU export does not have unique StopPlace@id attributes
            if stop_place.id == 'LU::StopPlace:0_CdT::':
                stop_place.id = getId(StopPlace, codespace, hashlib.md5(stop_place.name.value.encode()).hexdigest()[0:5])

            stop_place_id[stop_place.id] = stop_place

            if check_national_grid00(stop_place.centroid.location):
                continue

            stop_place_hash[get_location_hash(stop_place.centroid.location)] = stop_place
            stop_place_name[stop_place.name.value.split(', Gare')[0].split(', ')[-1].split('-')[0]] = stop_place

            if stop_place.quays is not None:
                for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                    quay_to_sp[quay.id] = stop_place.id

        ssp_to_quay = {}
        ssp_to_sp = {}
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}PassengerStopAssignment"):
            passenger_stop_assignment: PassengerStopAssignment = parser.parse(element, PassengerStopAssignment)
            if passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay is not None:
                ssp_to_quay[passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref
                if passenger_stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref != 'LU::StopPlace:0_CdT::':
                    ssp_to_sp[passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = passenger_stop_assignment.taxi_rank_ref_or_stop_place_ref_or_stop_place.ref

        ssp_hash = {}
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
            scheduled_stop_point: ScheduledStopPoint = parser.parse(element, ScheduledStopPoint)

            if '_CFL_' in scheduled_stop_point.id:
                uic = scheduled_stop_point.id.split(':')[3].split('_')[0]
                location = stations.get(uic, None)
                if location:
                    scheduled_stop_point.location = location

            if check_national_grid00(scheduled_stop_point.location):
                scheduled_stop_point.location = None

            if scheduled_stop_point.id in ssp_to_sp:
                stop_place = stop_place_id[ssp_to_sp[scheduled_stop_point.id]]

            elif scheduled_stop_point.id in ssp_to_quay:
                quay_ref = ssp_to_quay[scheduled_stop_point.id]
                if quay_ref in quay_to_sp:
                    stop_place = stop_place_id[quay_to_sp[quay_ref]]

            if stop_place is None:
                if scheduled_stop_point.location is not None:
                    stop_place = stop_place_hash.get(get_location_hash(scheduled_stop_point.location))

            if stop_place is None:
                stop_place = stop_place_name.get(scheduled_stop_point.short_name.value.split(', Gare')[0].split('-')[0])

            if stop_place is None:
                print(scheduled_stop_point.short_name.value)

            else:
                if scheduled_stop_point.location is None:
                    scheduled_stop_point.location = stop_place.centroid.location


                psa = PassengerStopAssignment(id=stop_place.id.replace("StopPlace", "PassengerStopAssignment"),
                                              taxi_rank_ref_or_stop_place_ref_or_stop_place=getRef(stop_place),
                                              taxi_stand_ref_or_quay_ref_or_quay=ssp_to_quay.get(scheduled_stop_point.id, None),
                                              fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(scheduled_stop_point))

                psas[psa.id] = psa

                # stop_1 = list(GtfsProfile.projectQuayStop(stop_place))
                # stops[stop_1[0]['stop_id']] = stop_1[0]
                stop_place = None

            if scheduled_stop_point.id not in stops:
                stop = GtfsProfile.projectScheduledStopPointToStop(scheduled_stop_point, stop_place)
                if stop is not None:
                    stops[stop['stop_id']] = stop

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}UicOperatingPeriod"):
            uic_operating_period: UicOperatingPeriod = parser.parse(element, UicOperatingPeriod)
            operational_dates = NordicProfile.getOperationalDates(uic_operating_period)
            if operational_dates[-1] > max_date:
                max_date = operational_dates[-1]
            uic_operating_periods[uic_operating_period.id] = operational_dates

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DayTypeAssignment"):
            day_type_assignment: DayTypeAssignment = parser.parse(element, DayTypeAssignment)
            calendar_dates[day_type_assignment.day_type_ref.ref] = list(
                GtfsProfile.getCalendarDates(day_type_assignment.day_type_ref.ref,
                                             uic_operating_periods[day_type_assignment.uic_operating_period_ref_or_operating_period_ref_or_operating_day_ref_or_date.ref]))

        
        trips = []
        stop_times = []
        service_journey_patterns = []
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourneyPattern"):
            service_journey_pattern: ServiceJourneyPattern = parser.parse(element, ServiceJourneyPattern)
            service_journey_patterns.append(service_journey_pattern)

        service_journey_patterns_index = getIndex(service_journey_patterns)

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
            service_journey: ServiceJourney = parser.parse(element, ServiceJourney)
            # CallsProfile.getCalls(service_journey, service_journey_patterns_index)
            service_journey_pattern = service_journey_patterns_index.get(service_journey.journey_pattern_ref.ref)
            trip = GtfsProfile.projectServiceJourneyToTrip(service_journey, service_journey_pattern)
            trips.append(trip)

            CallsProfile.getCallsFromTimetabledPassingTimes(service_journey, service_journey_pattern)
            stop_times += list(GtfsProfile.projectServiceJourneyToStopTimes(service_journey))

        GtfsProfile.writeToFile('/tmp/trips.txt', trips)
        GtfsProfile.writeToFile('/tmp/stop_times.txt', stop_times)

    GtfsProfile.writeToFile('/tmp/routes.txt', list(routes.values()), write_header=True)
    GtfsProfile.writeToFile('/tmp/agency.txt', [y for x, y in agencies.items() if x in used_agencies], write_header=True)
    GtfsProfile.writeToFile('/tmp/stops.txt', list(stops.values()), write_header=True)
    GtfsProfile.writeToFile('/tmp/calendar_dates.txt', [item for row in calendar_dates.values() for item in row], write_header=True)

    GtfsProfile.writeToFile('/tmp/feed_info.txt', [{
        'feed_publisher_name': 'openOV',
        'feed_publisher_url': 'http://openov.lu',
        'feed_lang': 'de',
        'default_lang': 'de',
        'feed_start_date': str(datetime.date.today()).replace('-', ''),
        'feed_end_date': str(max_date).replace('-', ''),
        'feed_version': str(datetime.date.today()).replace('-', ''),
        'feed_contact_email': '',
        'feed_contact_url': 'http://openov.lu/'
    }], write_header=True)


convert()

