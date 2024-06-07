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

from timetabledpassingtimesprofile import TimetablePassingTimesProfile


def get_location_hash(location: LocationStructure2, digits=5):
    return str(location.latitude)[0:5] + '_' + str(location.longitude)[0:5]

def check_national_grid00(location: LocationStructure2):
    if location is None:
        return True
    return str(location.latitude)[0:6] == '48.930' and str(location.longitude)[0:6] == '5.0770'

import csv

def convert():
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

    for input_filename in glob.glob("/tmp/NeTEx_CXX_HWGO_20240213_2024-02-18_202400046_baseline.xml.gz"):
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

            CallsProfile.getCalls(service_journey, service_journey_pattern)
            stop_times += list(GtfsProfile.projectServiceJourneyToStopTimes(service_journey))


        timetabledpassingtimesprofile = TimetablePassingTimesProfile(codespace, version, service_journeys,
                                                                     service_journey_patterns)
        timetabledpassingtimesprofile.getTimetabledPassingTimes(clean=True)


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

