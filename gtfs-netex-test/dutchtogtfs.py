import datetime
import glob
from typing import List, Set

from pyproj import Transformer
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler

from statistics import median

import lxml
import hashlib

from xsdata.models.datatype import XmlDate

from callsprofile import CallsProfile
from gtfsprofile import GtfsProfile
from netex import Line, StopPlace, Codespace, ScheduledStopPoint, LocationStructure2, PassengerStopAssignment, \
    Authority, Operator, Branding, UicOperatingPeriod, DayTypeAssignment, ServiceJourney, ServiceJourneyPattern, \
    TimeDemandType, Route, Quay, SimplePointVersionStructure, Pos, StopArea, AvailabilityCondition, RouteLink
from nordicprofile import NordicProfile
from refs import getId, getRef, getIndex

from decimal import Decimal

from servicecalendarepip import ServiceCalendarEPIPFrame
from timetabledpassingtimesprofile import TimetablePassingTimesProfile

import csv

def convert():
    context = XmlContext()
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

    stops = {}
    stop_places = []
    psa_ssp_stop = {}
    psa_quay_stop = {}

    """
    tree = lxml.etree.parse("/tmp/openov-20230711.xml.gz")
    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}StopPlace"):
        stop_place: StopPlace = parser.parse(element, StopPlace)
        stop_places.append(stop_place)
        if stop_place.quays:
            for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay:
                if isinstance(quay, Quay):
                    psa_quay_stop[quay.id] = stop_place.id
        if not stop_place.centroid and stop_place.quays:
            x = median([quay.centroid.location.pos.value[0] for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay])
            y = median([quay.centroid.location.pos.value[1] for quay in stop_place.quays.taxi_stand_ref_or_quay_ref_or_quay])
            stop_place.centroid = SimplePointVersionStructure(location=LocationStructure2(pos=Pos(value=[x, y])))

    stop_place_index = getIndex(stop_places)

    for element in tree.iterfind(".//{http://www.netex.org.uk/netex}PassengerStopAssignment"):
        try:
            passenger_stop_assignment: PassengerStopAssignment = parser.parse(element, PassengerStopAssignment)
            psa_ssp_stop[passenger_stop_assignment.fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point.ref] = stop_place_index.get(psa_quay_stop[passenger_stop_assignment.taxi_stand_ref_or_quay_ref_or_quay.ref])
        except:
            pass
    """
    # codespace: Codespace = Codespace(id="N", xmlns="LU")

    agencies = {}
    used_agencies = set([])
    routes = {}
    psas = {}
    uic_operating_periods = {}
    max_date = datetime.date.today()
    calendar_dates = {}

    GtfsProfile.writeToFile('/tmp/trips.txt', [GtfsProfile.empty_trip], write_header=True)
    GtfsProfile.writeToFile('/tmp/stop_times.txt', [GtfsProfile.empty_stop_time], write_header=True)
    GtfsProfile.writeToFile('/tmp/shapes.txt', [GtfsProfile.empty_shapes], write_header=True)

    # TODO: do something with default projection
    transformer = Transformer.from_crs("EPSG:28992", "EPSG:4326")

    for input_filename in glob.glob("/tmp/NeTEx_CXX_HWGO_20240213_2024-02-18_202400046_baseline.xml.gz"):
        tree = lxml.etree.parse(input_filename)

        route_links = {}
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}RouteLink"):
            route_link: RouteLink = parser.parse(element, RouteLink)
            route_links[route_link.id] = route_link

        netex_routes = []

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Route"):
            route: Route = parser.parse(element, Route)
            route_links_for_route = [route_links[por.onward_route_link_ref.ref] for por in route.points_in_sequence.point_on_route if por.onward_route_link_ref]
            shapes = list(GtfsProfile.projectRouteLinksToShapes(route, route_links_for_route, transformer))
            GtfsProfile.writeToFile('/tmp/shapes.txt', shapes)
            netex_routes.append(route)



        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Authority"):
            authority: Authority = parser.parse(element, Authority)
            agency = GtfsProfile.projectAuthorityToAgency(authority)
            agencies[agency['agency_id']] = agency

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Operator"):
            operator: Operator = parser.parse(element, Operator)
            agency = GtfsProfile.projectOperatorToAgency(operator)
            agencies[agency['agency_id']] = agency


        # DayType route
        """
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}DayTypeAssignment"):
            day_type_assignment: DayTypeAssignment = parser.parse(element, DayTypeAssignment)
            dates = calendar_dates.get(day_type_assignment.day_type_ref.ref, set([]))
            if isinstance(day_type_assignment.choice, XmlDate):
                dates.add(day_type_assignment.choice)
            calendar_dates[day_type_assignment.day_type_ref.ref] = dates

        calendar_dates2 = []
        
        for service_id, dates in calendar_dates.items():
            calendar_dates2 += list(GtfsProfile.getCalendarDates(service_id, sorted(list(dates))))
        """


        # AvailabilityCondition route

        """
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
            scheduled_stop_point: ScheduledStopPoint = parser.parse(element, ScheduledStopPoint)
            stop_place = psa_ssp_stop.get(scheduled_stop_point.id, None)
            if stop_place:
                stop = list(GtfsProfile.projectQuayStop(stop_place, with_quays=False, transformer=transformer))
                stops[stop[0]['stop_id']] = stop[0]
            stop = GtfsProfile.projectScheduledStopPointToStop(scheduled_stop_point, stop_place, transformer)
            stops[stop['stop_id']] = stop 
        """

        stop_areas_ssps: dict[str, List[ScheduledStopPoint]] = {}
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ScheduledStopPoint"):
            scheduled_stop_point: ScheduledStopPoint = parser.parse(element, ScheduledStopPoint)
            parent = None
            if scheduled_stop_point.stop_areas:
                parent = scheduled_stop_point.stop_areas.stop_area_ref[0]
                ssps = stop_areas_ssps.get(parent.ref, [])
                ssps.append(scheduled_stop_point)
                stop_areas_ssps[parent.ref] = ssps

            stop = GtfsProfile.projectScheduledStopPointToStop(scheduled_stop_point, parent, transformer)
            stops[stop['stop_id']] = stop

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}StopArea"):
            stop_area: StopArea = parser.parse(element, StopArea)
            ssps = stop_areas_ssps.get(stop_area.id, None)

            x = median([ssp.location.pos.value[0] for ssp in ssps])
            y = median([ssp.location.pos.value[1] for ssp in ssps])
            stop_area.centroid = SimplePointVersionStructure(location=LocationStructure2(pos=Pos(value=[x, y])))

            stop = GtfsProfile.projectStopAreaStop(stop_area, transformer=transformer)
            stops[stop['stop_id']] = stop

        # TODO: GTFS does not support Branding, so in order to facilitate it we will make it a separate Agency
        # A branding must have an 'original' agency or authority
        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Branding"):
            branding: Branding = parser.parse(element, Branding)
            agency = GtfsProfile.projectBrandingToAgency(branding)
            agencies[agency['agency_id']] = agency

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}Line"):
            line: Line = parser.parse(element, Line)
            route = GtfsProfile.projectLineToRoute(line)
            routes[route['route_id']] = route
            used_agencies.add(route['agency_id'])


        trips = []
        stop_times = []
        service_journey_patterns = []
        time_demand_types = []
        netex_routes_index: dict[str, Route] = getIndex(netex_routes)

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourneyPattern"):
            service_journey_pattern: ServiceJourneyPattern = parser.parse(element, ServiceJourneyPattern)
            service_journey_patterns.append(service_journey_pattern)

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}TimeDemandType"):
            time_demand_type: TimeDemandType = parser.parse(element, TimeDemandType)
            time_demand_types.append(time_demand_type)


        availability_conditions = {}

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}AvailabilityCondition"):
            availability_condition: AvailabilityCondition = parser.parse(element, AvailabilityCondition)
            availability_conditions[availability_condition.id] = availability_condition


        service_journey_patterns_index = getIndex(service_journey_patterns)
        time_demand_types_index = getIndex(time_demand_types)

        used_availability_conditions = {}

        for element in tree.iterfind(".//{http://www.netex.org.uk/netex}ServiceJourney"):
            service_journey: ServiceJourney = parser.parse(element, ServiceJourney)
            service_journey_pattern = service_journey_patterns_index.get(service_journey.journey_pattern_ref.ref)
            time_demand_type = time_demand_types_index.get(service_journey.time_demand_type_ref.ref)

            service_journey.choice = netex_routes_index[service_journey_pattern.route_ref_or_route_view.ref].line_ref
            service_journey.route_ref = getRef(netex_routes_index[service_journey_pattern.route_ref_or_route_view.ref])

            CallsProfile.getCallsFromTimeDemandType(service_journey,
                                                    service_journey_pattern,
                                                    time_demand_type)

            service_journey.day_types = None
            dates, _ = ServiceCalendarEPIPFrame.positiveAvailabilityCondition([availability_conditions[vc.ref] for vc in service_journey.validity_conditions_or_valid_between[0].choice])
            service_id = '+'.join([vc.ref for vc in service_journey.validity_conditions_or_valid_between[0].choice])
            operational_dates = [mydate.date() for mydate in dates]
            used_availability_conditions[service_id] = operational_dates
            if operational_dates[-1] > max_date:
                max_date = operational_dates[-1]

            trip = GtfsProfile.projectServiceJourneyToTrip(service_journey, service_journey_pattern)
            # trips.append(trip)

            stop_times = list(GtfsProfile.projectServiceJourneyToStopTimes(service_journey))

            GtfsProfile.writeToFile('/tmp/trips.txt', [trip])
            GtfsProfile.writeToFile('/tmp/stop_times.txt', stop_times)

        calendar_dates2 = []
        for service_id, dates in used_availability_conditions.items():
            calendar_dates2 += list(GtfsProfile.getCalendarDates(service_id, sorted(list(dates))))

    GtfsProfile.writeToFile('/tmp/routes.txt', list(routes.values()), write_header=True)
    GtfsProfile.writeToFile('/tmp/agency.txt', [y for x, y in agencies.items() if x in used_agencies], write_header=True)
    GtfsProfile.writeToFile('/tmp/stops.txt', list(stops.values()), write_header=True)
    GtfsProfile.writeToFile('/tmp/calendar_dates.txt', calendar_dates2, write_header=True)

    GtfsProfile.writeToFile('/tmp/feed_info.txt', [{
        'feed_publisher_name': 'openOV',
        'feed_publisher_url': 'http://openov.nl',
        'feed_lang': 'nl',
        'default_lang': 'nl',
        'feed_start_date': str(datetime.date.today()).replace('-', ''),
        'feed_end_date': str(max_date).replace('-', ''),
        'feed_version': str(datetime.date.today()).replace('-', ''),
        'feed_contact_email': '',
        'feed_contact_url': 'http://openov.nl/'
    }], write_header=True)


convert()

