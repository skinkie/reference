from decimal import Decimal
from typing import List

from xsdata.models.datatype import XmlDuration

from netex import StopArea, ScheduledStopPoint, StopPointInJourneyPattern, TimingPointInJourneyPattern, TimeDemandType, \
    ServiceJourney, AvailabilityCondition, Operator, Line, DestinationDisplay, MultilingualString, LocationStructure2, \
    Quay, PrivateCodeStructure, StopAreaRefsRelStructure, StopAreaRefStructure, ServiceJourneyPattern, \
    ValidityConditionsRelStructure, PointsInJourneyPatternRelStructure, DestinationDisplayView, ScheduledStopPointRef, \
    JourneyRunTimesRelStructure, JourneyRunTime, ServiceLinkRefStructure, TimingLinkRef, JourneyWaitTimesRelStructure, \
    JourneyWaitTime, ServiceJourneyPatternRef, TimeDemandTypeRef, SimplePointVersionStructure, ContactStructure, \
    PresentationStructure, StopPlace, PassengerStopAssignment, StopPlaceRef, Locale

stop_place: List[StopPlace] = [StopPlace(
    id="", version="",
    name=MultilingualString(value='Name'),
    centroid=SimplePointVersionStructure(location=LocationStructure2(latitude=Decimal(1.0), longitude=Decimal(2.0))),
    locale=Locale(time_zone_offset=Decimal(2.0))
)]
passenger_stop_assignments: List[PassengerStopAssignment] = [
    PassengerStopAssignment(
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(ref="1", version="1"),
        taxi_rank_ref_or_stop_place_ref_or_stop_place=StopPlaceRef(ref="1", version="1")
    )
]

scheduled_stop_points: List[ScheduledStopPoint] = [ScheduledStopPoint(
    id="", version="",
    name=MultilingualString(value='Name'),
    public_code=PrivateCodeStructure(),
    location=LocationStructure2(latitude=Decimal(1.0), longitude=Decimal(2.0))
)]

lines: List[Line] = [Line(
    id="", version="",
    name=MultilingualString(value="Line"),
    public_code="Code",
    presentation=PresentationStructure(text_colour="000000", background_colour="FFFFFF")
)]

service_journey_patterns: List[ServiceJourneyPattern] = [ServiceJourneyPattern(
    id="", version="",
    validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[AvailabilityCondition(valid_day_bits="10110")])],

    points_in_sequence=PointsInJourneyPatternRelStructure(point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=
                                                          [StopPointInJourneyPattern(order=1,
                                                                                     onward_timing_link_ref=TimingLinkRef(ref="1", version="1"),
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(ref="RefToStopPoint", version='1'),
                                                                                     for_boarding=True, for_alighting=False,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="Front Text")))])
)]

time_deband_types: List[TimeDemandType] = [TimeDemandType(
    id="", version="",
    run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(run_time=XmlDuration(value="PT0S"), timing_link_ref=TimingLinkRef(ref="1", version="1"))]),
    wait_times=JourneyWaitTimesRelStructure(journey_wait_time=[JourneyWaitTime(choice=ScheduledStopPointRef(ref="RefToStopPoint", version='1'), wait_time=XmlDuration(value="PT0S"))])
)]

service_journey: List[ServiceJourney] = [ServiceJourney(
    id="", version="",
    validity_conditions_or_valid_between=[
        ValidityConditionsRelStructure(choice=[AvailabilityCondition(valid_day_bits="10110")])],
    journey_pattern_ref=ServiceJourneyPatternRef(ref="1", version="1"),
    time_demand_type_ref=TimeDemandTypeRef(ref="1", version="1")
)]

operators: List[Operator] = [Operator(
    id="", version="",
    name=MultilingualString(value='Name'),
    contact_details=ContactStructure(url="http://example.com/")
)]

for scheduled_stop_point in scheduled_stop_points:
    scheduled_stop_point.location.longitude
    scheduled_stop_point.location.latitude

for scheduled_stop_point in scheduled_stop_points:
    scheduled_stop_point.stop_areas.stop_area_ref[0]

for service_journey_pattern in service_journey_patterns:
    for spijp in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
        spijp.scheduled_stop_point_ref

for service_journey_pattern in service_journey_patterns:
    for spijp in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
        spijp.destination_display_ref_or_destination_display_view.front_text

for service_journey_pattern in service_journey_patterns:
    for spijp in service_journey_pattern.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
        spijp.is_wait_point, spijp.for_boarding, spijp.for_alighting




# For boarding, For alighting, TimingPoint
StopPointInJourneyPattern()
TimingPointInJourneyPattern()

TimeDemandType()

ServiceJourney()

# TODO: Transfers
# TODO: vj_interlines

At ServiceJourney: AvailabilityCondition()

At ServiceJourneyPattern: AvailabilityCondition()

StopArea()

Operator()

# Commercial Modes

# Physical Modes

# Routes

Line()

DestinationDisplayRef() (JPP)



