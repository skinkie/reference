from decimal import Decimal
from typing import List

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDuration, XmlDateTime, XmlTime

from netex import StopArea, ScheduledStopPoint, StopPointInJourneyPattern, TimingPointInJourneyPattern, TimeDemandType, \
    ServiceJourney, AvailabilityCondition, Operator, Line, DestinationDisplay, MultilingualString, LocationStructure2, \
    Quay, PrivateCodeStructure, StopAreaRefsRelStructure, StopAreaRefStructure, ServiceJourneyPattern, \
    ValidityConditionsRelStructure, PointsInJourneyPatternRelStructure, DestinationDisplayView, ScheduledStopPointRef, \
    JourneyRunTimesRelStructure, JourneyRunTime, ServiceLinkRefStructure, TimingLinkRef, JourneyWaitTimesRelStructure, \
    JourneyWaitTime, ServiceJourneyPatternRef, TimeDemandTypeRef, SimplePointVersionStructure, ContactStructure, \
    PresentationStructure, StopPlace, PassengerStopAssignment, StopPlaceRef, Locale, PublicationDelivery, \
    CompositeFrame, FramesRelStructure, SiteFrame, StopPlacesInFrameRelStructure, ServiceFrame, \
    StopAssignmentsInFrameRelStructure, ScheduledStopPointsInFrameRelStructure, ResourceFrame, \
    OrganisationsInFrameRelStructure, TimetableFrame, LinesInFrameRelStructure, DataObjectsRelStructure, \
    JourneysInFrameRelStructure, JourneyPatternsInFrameRelStructure, TimeDemandTypesInFrameRelStructure, \
    TimingLinkRefStructure, PathLink, PathLinkEndStructure, PlaceRefStructure, TransferDurationStructure, \
    PathLinksInFrameRelStructure, DestinationDisplayRef, DestinationDisplaysInFrameRelStructure, \
    AllVehicleModesOfTransportEnumeration, OperatorRef, AccessibilityAssessment, LimitationStatusEnumeration, \
    AccessibilityLimitationsRelStructure, AccessibilityLimitation, WheelchairAccess, ParticipantRef, \
    SuitabilitiesRelStructure, Suitability, MobilityEnumeration, PyschosensoryNeedEnumeration, \
    PlaceEquipmentsRelStructure, ShelterEquipmentRef, CycleStorageEquipmentRef, CoveredEnumeration, \
    SiteRefsRelStructure, ParkingRef, Parking, ParkingVehicleEnumeration, ServiceFacilitySetsRelStructure, \
    ServiceFacilitySet, MobilityFacilityList, MobilityFacilityEnumeration, PassengerCommsFacilityList, \
    PassengerCommsFacilityEnumeration, PassengerInformationFacilityList, PassengerInformationFacilityEnumeration, \
    AssistanceFacilityList, AssistanceFacilityEnumeration, LuggageCarriageFacilityList, LuggageCarriageEnumeration, \
    SanitaryFacilityList, SanitaryFacilityEnumeration, FlexibleServiceProperties, FlexibleServiceEnumeration, \
    TransportSubmode, BusSubmode, BusSubmodeEnumeration, ServiceReservationFacilityList, ReservationEnumeration, \
    SuitableEnumeration, ParkingsInFrameRelStructure, QuaysRelStructure, QuayRef, RouteView, LineRef, \
    DestinationDisplayView, TimetabledPassingTimesRelStructure, TimetabledPassingTime, StopPointInJourneyPatternRef, \
    ValidBetween, Connection, ConnectionEndStructure, TransfersInFrameRelStructure, \
    JourneyInterchangesInFrameRelStructure, ServiceJourneyInterchange, VehicleJourneyRefStructure, ServiceJourneyRef, \
    PublicCodeStructure, RouteRef, Route, RoutesInFrameRelStructure, TypeOfProductCategoryRef, TypeOfProductCategory, \
    TypesOfValueInFrameRelStructure, OperatorView, VersionFrameDefaultsStructure, LocaleStructure

# Missing: BicycleRent

parkings: List[Parking] = [Parking(id="1", version="1", parking_vehicle_types=[ParkingVehicleEnumeration.CAR]),
    Parking(id="2", version="1", parking_vehicle_types=[ParkingVehicleEnumeration.CYCLE])
]
stop_places: List[StopPlace] = [StopPlace(
    id="1a1p", version="1",
    name=MultilingualString(value='Name'),
    centroid=SimplePointVersionStructure(location=LocationStructure2(latitude=Decimal('1.0'), longitude=Decimal('2.0'))),
    locale=Locale(time_zone_offset=Decimal('2.0')),
    covered=CoveredEnumeration.COVERED,
    adjacent_sites=SiteRefsRelStructure(site_ref_or_stop_place_ref=[ParkingRef(ref="1", version="1"), ParkingRef(ref="2", version="1")]),
    quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[Quay(id="1a1", version="1", accessibility_assessment=AccessibilityAssessment(
        id="1a1", version="1",
        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
        suitabilities=SuitabilitiesRelStructure(suitability=[
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=MobilityEnumeration.WHEELCHAIR),
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=PyschosensoryNeedEnumeration.VISUAL_IMPAIRMENT),
        ])),
),
                                                                Quay(id="1a3", version="1", accessibility_assessment=AccessibilityAssessment(
        id="1a3", version="1",
        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
        suitabilities=SuitabilitiesRelStructure(suitability=[
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=MobilityEnumeration.WHEELCHAIR),
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=PyschosensoryNeedEnumeration.VISUAL_IMPAIRMENT),
        ])),
),
                                                                Quay(id="1a5", version="1", accessibility_assessment=AccessibilityAssessment(
        id="1a5", version="1",
        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
        suitabilities=SuitabilitiesRelStructure(suitability=[
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=MobilityEnumeration.WHEELCHAIR),
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=PyschosensoryNeedEnumeration.VISUAL_IMPAIRMENT),
        ])),
)])
),
    StopPlace(
    id="1a2p", version="1",
    name=MultilingualString(value='Name'),
    centroid=SimplePointVersionStructure(location=LocationStructure2(latitude=Decimal('1.0'), longitude=Decimal('2.0'))),
    locale=Locale(time_zone_offset=Decimal('2.0')),
    covered=CoveredEnumeration.COVERED,
    adjacent_sites=SiteRefsRelStructure(stop_place_ref_or_site_ref=[ParkingRef(ref="1", version="1"), ParkingRef(ref="2", version="1")]),
    accessibility_assessment=AccessibilityAssessment(
        id="1a2p", version="1",
        mobility_impaired_access=LimitationStatusEnumeration.TRUE,
        suitabilities=SuitabilitiesRelStructure(suitability=[
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=MobilityEnumeration.WHEELCHAIR),
            Suitability(suitable=SuitableEnumeration.SUITABLE, mobility_need_or_psychosensory_need_or_medical_need_or_encumbrance_need=PyschosensoryNeedEnumeration.VISUAL_IMPAIRMENT),
        ])),
    quays=QuaysRelStructure(taxi_stand_ref_or_quay_ref_or_quay=[Quay(id="1a2", version="1"),
                                                                Quay(id="1a4", version="1"),
                                                                Quay(id="1a6", version="1")])
)
]


passenger_stop_assignments: List[PassengerStopAssignment] = [
    PassengerStopAssignment(
        id="1a1", version="1", order=1,
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(ref="1a1", version="1"),
        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref="1a1", version="1"),
    ),
    PassengerStopAssignment(
        id="1a3", version="1", order=1,
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(ref="1a3", version="1"),
        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref="1a3", version="1"),
    ),
    PassengerStopAssignment(
        id="1a5", version="1", order=1,
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
            ref="1a5", version="1"),
        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref="1a5", version="1"),
    ),
    PassengerStopAssignment(
        id="1a2", version="1", order=1,
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
            ref="1a2", version="1"),
        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref="1a2", version="1"),
    ),
    PassengerStopAssignment(
        id="1a4", version="1", order=1,
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
            ref="1a4", version="1"),
        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref="1a4", version="1"),
    ),
    PassengerStopAssignment(
        id="1a6", version="1", order=1,
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=ScheduledStopPointRef(
            ref="1a6", version="1"),
        taxi_stand_ref_or_quay_ref_or_quay=QuayRef(ref="1a6", version="1"),
    )
]

scheduled_stop_points: List[ScheduledStopPoint] = [ScheduledStopPoint(
    id="1a1", version="1",
    name=MultilingualString(value='Stop 1a1'),
    public_code=PublicCodeStructure(value="Platform code"),
    location=LocationStructure2(latitude=Decimal('1.101'), longitude=Decimal('1.1')),
),
    ScheduledStopPoint(
    id="1a2", version="1",
    name=MultilingualString(value='Stop 1a2'),
    location=LocationStructure2(latitude=Decimal('1.102'), longitude=Decimal('1.1'))
),
    ScheduledStopPoint(
    id="1a3", version="1",
    name=MultilingualString(value='Stop 1a3'),
    location=LocationStructure2(latitude=Decimal('1.103'), longitude=Decimal('1.1'))
),
    ScheduledStopPoint(
    id="1a4", version="1",
    name=MultilingualString(value='Stop 1a4'),
    location=LocationStructure2(latitude=Decimal('1.104'), longitude=Decimal('1.1'))
),
    ScheduledStopPoint(
    id="1a5", version="1",
    name=MultilingualString(value='Stop 1a5'),
    location=LocationStructure2(latitude=Decimal('1.105'), longitude=Decimal('1.1'))
),
    ScheduledStopPoint(
    id="1a6", version="1",
    name=MultilingualString(value='Stop 1a6'),
    location=LocationStructure2(latitude=Decimal('1.106'), longitude=Decimal('1.1'))
),
]

lines: List[Line] = [Line(
    id="1a|bus", version="1",
    name=MultilingualString(value="Bus"),
    transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
    public_code=PublicCodeStructure(value="Bus"),
    operator_ref=OperatorRef(ref="MMRI", version="1"),
    type_of_product_category_ref=TypeOfProductCategoryRef(ref="Standaard", version="1"),
    presentation=PresentationStructure(text_colour="000000", background_colour="FFFFFF")
),
Line(
    id="1a|ferry", version="1",
    name=MultilingualString(value="Ferry"),
    transport_mode=AllVehicleModesOfTransportEnumeration.FERRY,
    public_code=PublicCodeStructure(value="Ferry"),
    operator_ref=OperatorRef(ref="MMRI", version="1"),
    type_of_product_category_ref=TypeOfProductCategoryRef(ref="Standaard", version="1"),
    presentation=PresentationStructure(text_colour="000000", background_colour="FFFFFF")
),
Line(
    id="1a|rail", version="1",
    name=MultilingualString(value="Rail"),
    transport_mode=AllVehicleModesOfTransportEnumeration.RAIL,
    public_code=PublicCodeStructure(value="Rail"),
    operator_ref=OperatorRef(ref="MMRI", version="1"),
    type_of_product_category_ref=TypeOfProductCategoryRef(ref="Standaard", version="1"),
    presentation=PresentationStructure(text_colour="000000", background_colour="FFFFFF")
)]

type_of_product_categorys: List[TypeOfProductCategory] = [
    TypeOfProductCategory(id="Standaard", version="1", name=MultilingualString(value="Standaard"))
]

routes: List[Route] = [Route(id="1a|bus", version="1", line_ref=LineRef(ref="1a|bus", version="1")),
                       Route(id="1a|ferry", version="1", line_ref=LineRef(ref="1a|ferry", version="1")),
                       Route(id="1a|rail", version="1", line_ref=LineRef(ref="1a|rail", version="1"))]

service_journey_patterns: List[ServiceJourneyPattern] = [ServiceJourneyPattern(
    id="1a|bus", version="1",
    route_ref_or_route_view=RouteRef(ref="1a|bus", version="1"),
    validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[AvailabilityCondition(
        id="1a|bus", version="1",
        valid_day_bits="1", from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))])],
    points_in_sequence=PointsInJourneyPatternRelStructure(point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=
                                                          [StopPointInJourneyPattern(id="1a|bus", version="1", order=1,
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(ref="1a1", version='1'),
                                                                                     for_boarding=True, for_alighting=False,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="1a|bus"))),
                                                           StopPointInJourneyPattern(id="1a|bus", version="1", order=2,
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(
                                                                                         ref="1a2",
                                                                                         version='1'),
                                                                                     for_boarding=False,
                                                                                     for_alighting=True,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="1a|bus")))
                                                           ])
),
ServiceJourneyPattern(
    id="1a|ferry", version="1",
    route_ref_or_route_view=RouteRef(ref="1a|ferry", version="1"),
    validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[AvailabilityCondition(
        id="1a|ferry", version="1",
        valid_day_bits="1", from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))])],
    points_in_sequence=PointsInJourneyPatternRelStructure(point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=
                                                          [StopPointInJourneyPattern(id="1a|ferry", version="1", order=1,
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(ref="1a3", version='1'),
                                                                                     for_boarding=True, for_alighting=False,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="1a|ferry"))),
                                                           StopPointInJourneyPattern(id="1a|ferry", version="1", order=2,
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(
                                                                                         ref="1a4",
                                                                                         version='1'),
                                                                                     for_boarding=False,
                                                                                     for_alighting=True,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="1a|ferry")))
                                                           ])
),
ServiceJourneyPattern(
    id="1a|rail", version="1",
    route_ref_or_route_view=RouteRef(ref="1a|rail", version="1"),
    validity_conditions_or_valid_between=[ValidityConditionsRelStructure(choice=[AvailabilityCondition(
        id="1a|rail", version="1",
        valid_day_bits="1", from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))])],
    points_in_sequence=PointsInJourneyPatternRelStructure(point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=
                                                          [StopPointInJourneyPattern(id="1a|rail", version="1", order=1,
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(ref="1a5", version='1'),
                                                                                     for_boarding=True, for_alighting=False,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="1a|rail"))),
                                                           StopPointInJourneyPattern(id="1a|rail", version="1", order=2,
                                                                                     scheduled_stop_point_ref=ScheduledStopPointRef(
                                                                                         ref="1a6",
                                                                                         version='1'),
                                                                                     for_boarding=False,
                                                                                     for_alighting=True,
                                                                                     is_wait_point=False,
                                                                                     destination_display_ref_or_destination_display_view=DestinationDisplayView(front_text=MultilingualString(value="1a|rail")))
                                                           ])
)

]

# TODO: appropriate_signage
service_journeys: List[ServiceJourney] = [ServiceJourney(
    id="1a|bus|1", version="1",
    validity_conditions_or_valid_between=[
        ValidityConditionsRelStructure(choice=[AvailabilityCondition(
            id="1a|bus|1", version="1",
            valid_day_bits="1", from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))])],
    journey_pattern_ref=ServiceJourneyPatternRef(ref="1a|bus", version="1"),
    passing_times=TimetabledPassingTimesRelStructure(timetabled_passing_time=[
        TimetabledPassingTime(id="1a|bus|1.1", version="1", departure_time=XmlTime(0, 1, 0), arrival_time=XmlTime(0, 1, 0), point_in_journey_pattern_ref=StopPointInJourneyPatternRef(ref="1a|bus", order=1, version="1")),
        TimetabledPassingTime(id="1a|bus|1.2", version="1", departure_time=XmlTime(0, 2, 0), arrival_time=XmlTime(0, 2, 0), point_in_journey_pattern_ref=StopPointInJourneyPatternRef(ref="1a|bus", order=2, version="1")),
    ]),
    transport_submode=TransportSubmode(choice=BusSubmode(value=BusSubmodeEnumeration.SCHOOL_BUS)),
    facilities=ServiceFacilitySetsRelStructure(service_facility_set_ref_or_service_facility_set=[
        ServiceFacilitySet(
            id="1a|bus|1", version="1",
            mobility_facility_list=MobilityFacilityList(value=[MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                           passenger_information_facility_list=PassengerInformationFacilityList(
                               value=[PassengerInformationFacilityEnumeration.PASSENGER_INFORMATION_DISPLAY,
                                      PassengerInformationFacilityEnumeration.STOP_ANNOUNCEMENTS]),
                           passenger_comms_facility_list=PassengerCommsFacilityList(value=[PassengerCommsFacilityEnumeration.FREE_WIFI]),
                           )
    ]),
    flexible_service_properties_ref_or_flexible_service_properties=FlexibleServiceProperties(flexible_service_type=FlexibleServiceEnumeration.FIXED_PASSING_TIMES)
),
ServiceJourney(
    id="1a|ferry|1", version="1",
    validity_conditions_or_valid_between=[
        ValidityConditionsRelStructure(choice=[AvailabilityCondition(
            id="1a|ferry|1", version="1",
            valid_day_bits="1", from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))])],
    journey_pattern_ref=ServiceJourneyPatternRef(ref="1a|ferry", version="1"),
    passing_times=TimetabledPassingTimesRelStructure(timetabled_passing_time=[
        TimetabledPassingTime(id="1a|ferry|1.1", version="1", departure_time=XmlTime(0, 3, 0), arrival_time=XmlTime(0, 3, 0), point_in_journey_pattern_ref=StopPointInJourneyPatternRef(ref="1a|ferry", order=1, version="1")),
        TimetabledPassingTime(id="1a|ferry|1.2", version="1", departure_time=XmlTime(0, 4, 0), arrival_time=XmlTime(0, 4, 0), point_in_journey_pattern_ref=StopPointInJourneyPatternRef(ref="1a|ferry", order=2, version="1")),
    ]),
    facilities=ServiceFacilitySetsRelStructure(service_facility_set_ref_or_service_facility_set=[
        ServiceFacilitySet(
            id="1a|ferry|1", version="1",
            mobility_facility_list=MobilityFacilityList(value=[MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                           luggage_carriage_facility_list=LuggageCarriageFacilityList(value=[LuggageCarriageEnumeration.CYCLES_ALLOWED]),
                           passenger_information_facility_list=PassengerInformationFacilityList(
                               value=[PassengerInformationFacilityEnumeration.PASSENGER_INFORMATION_DISPLAY,
                                      PassengerInformationFacilityEnumeration.STOP_ANNOUNCEMENTS]),
                           assistance_facility_list=AssistanceFacilityList(value=[AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]),
                           passenger_comms_facility_list=PassengerCommsFacilityList(value=[PassengerCommsFacilityEnumeration.FREE_WIFI]),
                           sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET]),
                           )
    ]),
    flexible_service_properties_ref_or_flexible_service_properties=FlexibleServiceProperties(flexible_service_type=FlexibleServiceEnumeration.NOT_FLEXIBLE)
),
ServiceJourney(
    id="1a|rail|1", version="1",
    validity_conditions_or_valid_between=[
        ValidityConditionsRelStructure(choice=[AvailabilityCondition(
            id="1a|rail|1", version="1",
            valid_day_bits="1", from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))])],
    journey_pattern_ref=ServiceJourneyPatternRef(ref="1a|rail", version="1"),
    passing_times=TimetabledPassingTimesRelStructure(timetabled_passing_time=[
        TimetabledPassingTime(id="1a|rail|1.1", version="1", departure_time=XmlTime(0, 5, 0),
                              arrival_time=XmlTime(0, 5, 0),
                              point_in_journey_pattern_ref=StopPointInJourneyPatternRef(ref="1a|rail", order=1,
                                                                                        version="1")),
        TimetabledPassingTime(id="1a|rail|1.2", version="1", departure_time=XmlTime(0, 6, 0),
                              arrival_time=XmlTime(0, 6, 0),
                              point_in_journey_pattern_ref=StopPointInJourneyPatternRef(ref="1a|rail", order=2,
                                                                                        version="1")),
    ]),
    facilities=ServiceFacilitySetsRelStructure(service_facility_set_ref_or_service_facility_set=[
        ServiceFacilitySet(
            id="1a|rail|1", version="1",
            mobility_facility_list=MobilityFacilityList(value=[MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                           luggage_carriage_facility_list=LuggageCarriageFacilityList(value=[LuggageCarriageEnumeration.CYCLES_ALLOWED]),
                           passenger_information_facility_list=PassengerInformationFacilityList(
                               value=[PassengerInformationFacilityEnumeration.PASSENGER_INFORMATION_DISPLAY,
                                      PassengerInformationFacilityEnumeration.STOP_ANNOUNCEMENTS]),
                           assistance_facility_list=AssistanceFacilityList(value=[AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]),
                           passenger_comms_facility_list=PassengerCommsFacilityList(value=[PassengerCommsFacilityEnumeration.FREE_WIFI]),
                           sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET]),
                           service_reservation_facility_list=ServiceReservationFacilityList(value=[ReservationEnumeration.RESERVATIONS_COMPULSORY])
                           )
    ]),
    flexible_service_properties_ref_or_flexible_service_properties=FlexibleServiceProperties(flexible_service_type=FlexibleServiceEnumeration.NOT_FLEXIBLE)
)
]

operators: List[Operator] = [Operator(
    id="MMRI", version="1",
    name=MultilingualString(value='Multimodale Reisinformatie'),
    contact_details=ContactStructure(url="http://1313.nl/")
)]

"""
path_links: List[PathLink] = [PathLink(
    id="1", version="1",
    from_value=PathLinkEndStructure(place_ref=PlaceRefStructure(name_of_ref_class="Quay", ref="1a2", version="1")),
    to=PathLinkEndStructure(place_ref=PlaceRefStructure(name_of_ref_class="Quay", ref="1a3", version="1")),
    transfer_duration=TransferDurationStructure(default_duration=XmlDuration("PT0S"))
),
    PathLink(
        id="2", version="1",
        from_value=PathLinkEndStructure(place_ref=PlaceRefStructure(name_of_ref_class="Quay", ref="1a4", version="1")),
        to=PathLinkEndStructure(place_ref=PlaceRefStructure(name_of_ref_class="Quay", ref="1a5", version="1")),
        transfer_duration=TransferDurationStructure(default_duration=XmlDuration("PT0S"))
    )
]
"""

connections: List[Connection] = [Connection(
        id="1", version="1",
        from_value=ConnectionEndStructure(scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRef(ref="1a2", version="1")),
        to=ConnectionEndStructure(scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRef(ref="1a3", version="1")),
        transfer_duration=TransferDurationStructure(default_duration=XmlDuration("PT0S")),
        both_ways=True,
    ),
    Connection(
        id="2", version="1",
        from_value=ConnectionEndStructure(scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRef(ref="1a4", version="1")),
        to=ConnectionEndStructure(scheduled_stop_point_ref_or_vehicle_meeting_point_ref=ScheduledStopPointRef(ref="1a5", version="1")),
        transfer_duration=TransferDurationStructure(default_duration=XmlDuration("PT0S")),
        both_ways=True
    )
]

service_journey_interchanges: List[ServiceJourneyInterchange] = [ServiceJourneyInterchange(
    id="1", version="1",
    from_journey_ref=VehicleJourneyRefStructure(ref="1a|bus|1", version="1", name_of_ref_class="ServiceJourney"),
    to_journey_ref=VehicleJourneyRefStructure(ref="1a|rail|1", version="1", name_of_ref_class="ServiceJourney"),
    stay_seated=True
)]

resource_frame = ResourceFrame(id="1", version="1", organisations=OrganisationsInFrameRelStructure(organisation_or_transport_organisation=operators),
                               types_of_value=TypesOfValueInFrameRelStructure(choice=type_of_product_categorys))

site_frame = SiteFrame(id="1", version="1",
    stop_places=StopPlacesInFrameRelStructure(stop_place=stop_places),
                       parkings=ParkingsInFrameRelStructure(parking=parkings))
                       # path_links=PathLinksInFrameRelStructure(path_link=path_links))

service_frame = ServiceFrame(
    id="1", version="1",
    scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_points),
    connections=TransfersInFrameRelStructure(transfer=connections),
    stop_assignments=StopAssignmentsInFrameRelStructure(stop_assignment=passenger_stop_assignments),
    lines=LinesInFrameRelStructure(line=lines),
    routes=RoutesInFrameRelStructure(route=routes),
    journey_patterns=JourneyPatternsInFrameRelStructure(journey_pattern=service_journey_patterns)
)

timetable_frame = TimetableFrame(
    id="1", version="1",
    vehicle_journeys=JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=service_journeys),
    journey_interchanges=JourneyInterchangesInFrameRelStructure(service_journey_pattern_interchange_or_service_journey_interchange=service_journey_interchanges)
)

composite_frame: CompositeFrame = CompositeFrame(id="1", version="1",
                                                 validity_conditions_or_valid_between=[ValidBetween(from_date=XmlDateTime.from_string("2014-01-01T00:00:00"), to_date=XmlDateTime.from_string("2014-01-01T00:00:00"))],
                                                 frame_defaults=VersionFrameDefaultsStructure(default_locale=LocaleStructure(time_zone="Europe/Amsterdam")),
                                                 frames=FramesRelStructure(common_frame=[resource_frame, site_frame, service_frame, timetable_frame]))

publication_delivery: PublicationDelivery = PublicationDelivery(
    publication_timestamp=XmlDateTime.now(),
    participant_ref=ParticipantRef(value="rrrr"),
    data_objects=DataObjectsRelStructure(choice=[composite_frame]),
    version="ntx:1.1",
)

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

ns_map={'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

with open('/tmp/timetable4.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)

"""
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

"""


