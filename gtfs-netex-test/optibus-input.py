from decimal import Decimal
from typing import List, Dict

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.models.datatype import XmlDateTime, XmlTime
import datetime

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from netex import PublicationDelivery, PassengerCapacity, DataObjectsRelStructure, GeneralFrame, \
    GeneralFrameMembersRelStructure, ScheduledStopPoint, LocationStructure2, KeyList, MultilingualString, \
    StopAreaRefsRelStructure, StopAreaRefStructure, PrivateCode, ServiceJourney, CallsRelStructure, Call, \
    DepartureStructure, ScheduledStopPointRef, DayType, PropertiesOfDayRelStructure, PropertyOfDay, \
    DayOfWeekEnumeration, VehicleType, PassengerCapacitiesRelStructure, Extensions2, Line, Route, ServiceJourneyPattern, \
    DirectionTypeEnumeration, PointsInJourneyPatternRelStructure, StopPointInJourneyPattern, \
    TimingPointInJourneyPattern, TimingLinkRefStructure, TimingLink, LineString, PosList, RouteView, LineRef, \
    TimingPointRefStructure, ValidityConditionsRelStructure, AvailabilityCondition, DayTypesRelStructure, DayTypeRef, \
    ServiceJourneyPatternRef, OperatorRef, ParticipantRef
from netex import OnlineServiceOperatorVersionStructure
from optibus import StopsOfTimeplan, TripsOfRoute, ServicesOfTimeplan, VehicleTypesOfTimeplan, RoutesOfTimeplan
from optibus.routes_of_timeplan import StopsProperties, Patterns, Stops
from optibus.trips_of_route import TripTimes

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
# parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

ns_map = {None: 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
parser = JsonParser(context=context)

services: List[ServicesOfTimeplan] = parser.parse(open('optibus-input/services-of-timeplan.json', 'rb'), List[ServicesOfTimeplan])

def mapNumberToDayOfWeek(day: int):
    match day:
        case 1:
            return DayOfWeekEnumeration.SUNDAY
        case 2:
            return DayOfWeekEnumeration.MONDAY
        case 3:
            return DayOfWeekEnumeration.TUESDAY
        case 4:
            return DayOfWeekEnumeration.WEDNESDAY
        case 5:
            return DayOfWeekEnumeration.THURSDAY
        case 6:
            return DayOfWeekEnumeration.FRIDAY
        case 7:
            return DayOfWeekEnumeration.SATURDAY


day_types: List[DayType] = []
for service in services:
    day_types.append(DayType(id=service.id, version="1", name=MultilingualString(value=service.name),
                             properties=PropertiesOfDayRelStructure(property_of_day=
                                                                    [PropertyOfDay(name=service.name, days_of_week=[mapNumberToDayOfWeek(x) for x in service.days])])))


vehicletypes: List[VehicleTypesOfTimeplan] = parser.parse(open('optibus-input/vehicle-types-of-timeplan.json', 'rb'), List[VehicleTypesOfTimeplan])

vehicle_types: List[VehicleType] = []
for vehicle_type in vehicletypes:
    vehicle_types.append(VehicleType(id=vehicle_type.id, version="1", name=MultilingualString(value=vehicle_type.name),
                                     extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaximumSpeed", text=vehicle_type.speed)]), # see #635
                                     description=MultilingualString(value=vehicle_type.description), capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity=[PassengerCapacity(id=vehicle_type.id, total_capacity=vehicle_type.capacity)])))


def mapDirectionName(name):
    match name:
        case "INBOUND":
            return DirectionTypeEnumeration.INBOUND
        case "OUTBOUND":
            return DirectionTypeEnumeration.OUTBOUND

def mapPointInSequence(stop: Stops, pattern: Patterns):
    match stop.type_value:
        case 'time_point':
            return TimingPointInJourneyPattern(id=f"{pattern.id}-{stop.stop_id}-{stop.route_stop_index}", version="1",
                                                              order=stop.route_stop_index + 1,
                                                              timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref=ScheduledStopPointRef(ref=stop.stop_id,
                                                                                             version="1"))
        case 'bus_stop':
            return StopPointInJourneyPattern(id=f"{pattern.id}-{stop.stop_id}-{stop.route_stop_index}", version="1", order=stop.route_stop_index + 1,
                                             scheduled_stop_point_ref=ScheduledStopPointRef(ref=stop.stop_id, version="1"))

def mapPattern(pattern: Patterns, route_id: str, direction_type: DirectionTypeEnumeration):
    index = {x.stop_id: x for x in pattern.google_path}
    timing_links = []
    points_in_sequence = []
    for i in range(0, len(pattern.stops) - 1):
        stop = pattern.stops[i]
        stop_next = pattern.stops[i + 1]

        pos_list: List[float] = []
        for pair in index[stop_next.stop_id].path_to_check_point:
            pos_list += [pair.lat, pair.lng]

        pos_list += [index[stop_next.stop_id].checkpoint.lat, index[stop_next.stop_id].checkpoint.lng]

        distance = None
        if stop_next.distance_from_previous_stop == 0:
            distance = Decimal(stop_next.distance_from_previous_stop)

        timing_link = TimingLink(id=f"{pattern.id}-{stop.route_stop_index}", version="1",
                                 from_point_ref=TimingPointRefStructure(name_of_ref_class="ScheduledStopPoint", ref=stop.stop_id, version="1"),
                                 to_point_ref=TimingPointRefStructure(name_of_ref_class="ScheduledStopPoint", ref=stop_next.stop_id, version="1"),
                                 distance=distance,
                                 line_string=LineString(id=f"GML_{pattern.id}_{stop.route_stop_index}",
                                                        pos_or_point_property_or_pos_list=[PosList(srs_name="EPSG:4326", srs_dimension=2, count=len(pos_list) // 2, value=pos_list)]))

        timing_links.append(timing_link)
        pis = mapPointInSequence(stop, pattern)
        pis.onward_timing_link_ref = TimingLinkRefStructure(ref=f"{pattern.id}-{stop.route_stop_index}", version="1")
        points_in_sequence.append(pis)

    points_in_sequence.append(mapPointInSequence(pattern.stops[-1], pattern))

    sjp = ServiceJourneyPattern(id=pattern.id, version="1",
                                name=MultilingualString(value=pattern.name),
                                direction_type=direction_type,
                                route_ref_or_route_view=RouteView(flexible_line_ref_or_line_ref_or_line_view=LineRef(ref=route_id, version="1")),
                          points_in_sequence=PointsInJourneyPatternRelStructure(point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=points_in_sequence),
                          )

    return sjp, timing_links

routes_ob: List[RoutesOfTimeplan] = parser.parse(open('optibus-input/routes-of-timeplan.json', 'rb'), List[RoutesOfTimeplan])

service_journey_pattern: List[ServiceJourneyPattern] = []
lines: List[Line] = []
tls: List[TimingLink] = []
sjps: List[ServiceJourneyPattern] = []

for route in routes_ob:
    for direction in route.directions:
        if direction is None:
            continue

        for pattern in direction.patterns:
            sjp, timing_links = mapPattern(pattern, route.id, mapDirectionName(direction.name))
            sjps.append(sjp)
            tls += timing_links

    lines.append(Line(id=route.id, version="1", name=MultilingualString(value=route.sign), public_code=route.code, ))



stops: List[StopsOfTimeplan] = parser.parse(open('optibus-input/stops-of-timeplan.json', 'rb'), List[StopsOfTimeplan])

scheduled_stop_points: List[ScheduledStopPoint] = []

for stop in stops:
    naptan = None
    if stop.properties.naptan is not None and stop.properties.naptan.code is not None:
        naptan = PrivateCode(value=stop.properties.naptan.code, type_value="naptan")
    stop_areas = None
    if stop.properties.place is not None:
        stop_areas = StopAreaRefsRelStructure(stop_area_ref=[StopAreaRefStructure(ref=stop.properties.place, version="any")])
    scheduled_stop_points.append(ScheduledStopPoint(id=stop.id,
                                                    version="1",
                                                    changed=XmlDateTime.now(), # TODO: parse hidious last update format
                       name=MultilingualString(value=stop.name),
                                                    private_code=naptan,
                       public_code=stop.properties.stop_code,
                       location=LocationStructure2(longitude=stop.longitude,
                                                   latitude=stop.latitude),
                       stop_areas=stop_areas)
                       )


service_journeys: List[ServiceJourney] = []

def tripTimeToDeparure(trip_time: TripTimes):
    parts = trip_time.time.split(":")
    if len(parts) == 2:
        parts.append("00")

    day_offset = int(parts[0]) // 24
    parts[0] = "{:02d}".format((int(parts[0]) % 24))

    if day_offset == 0:
        day_offset = None

    return DepartureStructure(time=XmlTime.from_string(":".join(parts)), day_offset=day_offset)

trips: List[TripsOfRoute] = parser.parse(open('optibus-input/trips-of-route.json', 'rb'), List[TripsOfRoute])
for trip in trips:
    service_journeys.append(ServiceJourney(id=trip.id, version="1",
                                           validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[AvailabilityCondition(id=trip.id, version="1", day_types=DayTypesRelStructure(day_type_ref_or_day_type=[DayTypeRef(ref=trip.service_id, version="1")]))])],
                                           flexible_line_ref_or_line_ref_or_line_view_or_flexible_line_view=LineRef(ref=trip.route_id ,version="1"),
                                           operator_ref_or_operator_view=OperatorRef(ref=trip.properties.operator, version="1"),
                                           journey_pattern_ref=ServiceJourneyPatternRef(ref=trip.pattern_id, version="1"),
                                           calls=CallsRelStructure(call=[Call(id=f"{trip.id}-{trip_time.stop_index}",
                                                                              version="1",
                                                                              fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point_view=ScheduledStopPointRef(ref=trip_time.stop_id, version="1"),
                                                                              order=trip_time.stop_index + 1,
                                                                              departure=tripTimeToDeparure(trip_time)) for trip_time in trip.trip_times])))

general_frame = GeneralFrame(id="GeneralFrame", version="1",
                             members=GeneralFrameMembersRelStructure(choice=vehicle_types + lines + scheduled_stop_points + tls + sjps + day_types + service_journeys))

publication_delivery = PublicationDelivery(participant_ref=ParticipantRef(value="PyNeTExConv"),
                                           publication_timestamp=XmlDateTime.from_datetime(datetime.datetime.now()))
publication_delivery.version = "ntx:1.1"
publication_delivery.description = "NeTEx export"
publication_delivery.data_objects = DataObjectsRelStructure(choice=[general_frame])


serializer.write(open('/tmp/optibus.xml', 'w'), publication_delivery, ns_map)


