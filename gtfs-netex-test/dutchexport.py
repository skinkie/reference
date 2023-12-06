from _decimal import Decimal

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlDuration

from dutchprofile import DutchProfile
from netex import Codespace, Version, VersionTypeEnumeration, DataSource, MultilingualString, ResponsibilitySet, \
    ResponsibilityRoleAssignmentsRelStructure, ResponsibilityRoleAssignment, VersionOfObjectRefStructure, Operator, \
    AllModesEnumeration, OrganisationTypeEnumeration, OperatorActivitiesEnumeration, OperationalContext, \
    AllVehicleModesOfTransportEnumeration, VehicleType, FuelTypeEnumeration, PassengerCapacityStructure, \
    FareClassEnumeration, ServiceFacilitySetsRelStructure, ServiceFacilitySet, MobilityFacilityEnumeration, \
    SanitaryFacilityEnumeration, PassengerCommsFacilityEnumeration, VehicleAccessFacilityEnumeration, \
    AssistanceFacilityEnumeration, MealFacilityEnumeration, TransportAdministrativeZone, RoutePoint, RouteLink, Route, \
    Line, DestinationDisplay, ScheduledStopPoint, StopArea, PassengerStopAssignment, TimingLink, ServiceJourneyPattern, \
    TimeDemandType, TypeOfServiceRef, AccessibilityAssessment, LimitationStatusEnumeration, LocationStructure2, Pos, \
    DirectionTypeEnumeration, PointsOnRouteRelStructure, PointOnRoute, PrivateCode, \
    DestinationDisplayVariantsRelStructure, DestinationDisplayVariant, Extensions2, DeliveryVariantTypeEnumeration, \
    ProjectionsRelStructure, PointProjection, StopAreaRefsRelStructure, TopographicPlaceView, \
    PointsInJourneyPatternRelStructure, StopPointInJourneyPattern, JourneyRunTimesRelStructure, JourneyRunTime, \
    TimingLinkRefStructure, PointRefStructure, RoutePointRefStructure, TimingPointRefStructure, LineString, PosList, \
    PassengerCapacitiesRelStructure, PassengerCapacity, RouteLinkRefStructure
import datetime

from refs import getId, getRef

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

short_name = "TESO"

codespace = Codespace(id="{}:Codespace:{}".format(short_name, short_name), xmlns=short_name,
                      xmlns_url="https://teso.nl/", description=short_name)

start_date = datetime.datetime(year=2023, month=11, day=29)
end_date = datetime.datetime(year=2023, month=12, day=29)

version = Version(id=getId(Version, codespace, str(1)),
                  version=str(1),
                  start_date=XmlDateTime.from_datetime(start_date),
                  end_date=XmlDateTime.from_datetime(end_date),
                  version_type=VersionTypeEnumeration.BASELINE)

data_source = DataSource(id=getId(DataSource, codespace, short_name),
                         version=version.version,
                         name=MultilingualString(value=short_name),
                         short_name=MultilingualString(value=short_name),
                         description=MultilingualString(value=short_name))

transport_administrative_zone = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "TESO"),
                                                            version="any",
                                                            name=MultilingualString(value="TESO"),
                                                            short_name=MultilingualString(value="TESO"),
                                                            description=[MultilingualString(value="TESO")],
                                                            vehicle_modes=[AllModesEnumeration.FERRY])

responsibility_set = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, short_name),
                                       version=version.version,
                                       name=MultilingualString(value=short_name),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "TESO"),
                                                                        version=version.version,
                                                                        data_role_type=None,
                                                                        stakeholder_role_type=None,
                                                                        responsible_area_ref=getRef(transport_administrative_zone, VersionOfObjectRefStructure))
                                       ]))

organisation = Operator(id=getId(Operator, codespace, "TESO"), version=version.version,
                        company_number="37000097",
                        name=MultilingualString(value="TESO"),
                        short_name=MultilingualString(value="TESO"),
                        legal_name=MultilingualString(value="Koninklijke N.V. Texels Eigen Stoomboot Onderneming"),
                        organisation_type=[OrganisationTypeEnumeration.OPERATOR],
                        primary_mode=AllModesEnumeration.FERRY,
                        operator_activities=[OperatorActivitiesEnumeration.PASSENGER])

operational_context = OperationalContext(id=getId(OperationalContext, codespace, "WATER"), version=version.version,
                                       name=MultilingualString(value="WATER"), short_name=MultilingualString(value="WATER"),
                                         vehicle_mode=AllVehicleModesOfTransportEnumeration.FERRY)

vehicle_type = VehicleType(id=getId(VehicleType, codespace, "Texelstroom2"), version=version.version,
                           name=MultilingualString(value="Texelstroom (2)"),
                           description=MultilingualString(value="Hybride CNG/diesel-elektrische Ro-Ro ferry"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.NATURAL_GAS,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "Texelstroom2"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=1750)),
                           length=Decimal(value='135'), width=Decimal(value='27.90'), height=Decimal(value='7.18'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "Texelstroom2"), version=version.version,
                                                  mobility_facility_list=[MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                  passenger_comms_facility_list=[PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET, SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH, MealFacilityEnumeration.BREAKFAST, MealFacilityEnumeration.SNACK, MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                                                  )]
                           ))

dutchprofile = DutchProfile(codespace, data_source, responsibility_set, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set],
                                                 organisations=[organisation], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type], zones=[transport_administrative_zone])

line = Line(id=getId(Line, codespace, "TESO"), version=version.version, name=MultilingualString(value="TESO"),
              monitored=False,
              description=MultilingualString(value="Veer tussen Den Helder en Texel"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "TESO"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )


rp_dh = RoutePoint(id=getId(RoutePoint, codespace, "DH"), version=version.version, location=LocationStructure2(pos=Pos(value=[114066, 553040], srs_dimension=2)))
rp_tx = RoutePoint(id=getId(RoutePoint, codespace, "TX"), version=version.version, location=LocationStructure2(pos=Pos(value=[114311, 557575], srs_dimension=2)))

route_points = [rp_dh, rp_tx]

rl_dhtx = RouteLink(id=getId(RouteLink, codespace, "DH-TX"), version=version.version,
                    from_point_ref=getRef(rp_dh, RoutePointRefStructure), to_point_ref=getRef(rp_tx, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "DH-TX").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(value=(rp_dh.location.pos.value + rp_tx.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_txdh = RouteLink(id=getId(RouteLink, codespace, "TX-DH"), version=version.version,
                    from_point_ref=getRef(rp_tx, RoutePointRefStructure), to_point_ref=getRef(rp_dh, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "TX-DH").replace(":", "_").replace("-", "_"),
                        pos_or_point_property_or_pos_list=[PosList(value=rp_tx.location.pos.value + rp_dh.location.pos.value)]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_dhtx, rl_txdh]



route_dhtx = Route(id=getId(Route, codespace, "DH-TX"), version=version.version,
                   flexible_line_ref_or_line_ref=getRef(line),
                   direction_type=DirectionTypeEnumeration.INBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "DH-TX-DH"), version=version.version, order=1, choice_1=getRef(rp_dh), onward_route_link_ref=getRef(rl_dhtx, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "DH-TX-TX"), version=version.version, order=2, choice_1=getRef(rp_tx)),
                   ])
                   )

route_txdh = Route(id=getId(Route, codespace, "TX-DH"), version=version.version,
                   flexible_line_ref_or_line_ref=getRef(line),
                   direction_type=DirectionTypeEnumeration.OUTBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "TX-DH-TX"), version=version.version, order=1, choice_1=getRef(rp_tx), onward_route_link_ref=getRef(rl_txdh, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "TX-DH-DH"), version=version.version, order=2, choice_1=getRef(rp_dh)),
                   ])
                   )

routes = [route_dhtx, route_txdh]

lines = [line]

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_dh = DestinationDisplay(id=getId(DestinationDisplay, codespace, "DH"), version=version.version,
                           name=MultilingualString(value="Den Helder"),
                           front_text=MultilingualString(value="Den Helder"),
                           private_code=PrivateCode(value="1", type_value="DestinationCode"))
setVariants(dd_dh)

dd_tx = DestinationDisplay(id=getId(DestinationDisplay, codespace, "TX"), version=version.version,
                           name=MultilingualString(value="Texel"),
                           front_text=MultilingualString(value="Texel"),
                           private_code=PrivateCode(value="2", type_value="DestinationCode"))
setVariants(dd_tx)


destination_displays=[dd_dh, dd_tx]

sa_dh = StopArea(id=getId(StopArea, codespace, "DH"),
                 version=version.version,
                 name=MultilingualString(value="Den Helder"),
                 private_code=PrivateCode(value="1", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Den Helder"))
                 )

sa_tx = StopArea(id=getId(StopArea, codespace, "TX"),
                 version=version.version,
                 name=MultilingualString(value="Haven"),
                 private_code=PrivateCode(value="2", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="'t Horntje"))
                 )

stop_areas=[sa_dh, sa_tx]

ssp_dh_1 = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "DH-B"), version=version.version,
                              name=MultilingualString(value="Den Helder"),
                              location=LocationStructure2(pos=Pos(value=[114066, 553040], srs_dimension=2)),
                              projections=ProjectionsRelStructure(choice=[PointProjection(id=getId(PointProjection, codespace, "DH-B-1"), version=version.version, project_to_point_ref=getRef(rp_dh, PointRefStructure))]),
                              for_alighting=False, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_dh)]),
                              private_code=PrivateCode(value="1", type_value="UserStopCode"))

ssp_dh_2 = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "DH-A"), version=version.version,
                              name=MultilingualString(value="Den Helder"),
                              location=LocationStructure2(pos=Pos(value=[114066, 553040], srs_dimension=2)),
                              projections=ProjectionsRelStructure(choice=[PointProjection(id=getId(PointProjection, codespace, "DH-A-3"), version=version.version, project_to_point_ref=getRef(rp_dh, PointRefStructure))]),
                              for_alighting=True, for_boarding=False,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_dh)]),
                              private_code=PrivateCode(value="3", type_value="UserStopCode"))

ssp_tx_1 = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "TX-B"), version=version.version,
                              name=MultilingualString(value="Texel"),
                              location=LocationStructure2(pos=Pos(value=[114311, 557575], srs_dimension=2)),
                              projections=ProjectionsRelStructure(choice=[PointProjection(id=getId(PointProjection, codespace, "DH-B-2"), version=version.version, project_to_point_ref=getRef(rp_tx, PointRefStructure))]),
                              for_alighting=False, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_tx)]),
                              private_code=PrivateCode(value="2", type_value="UserStopCode"))

ssp_tx_2 = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "TX-A"), version=version.version,
                              name=MultilingualString(value="Texel"),
                              location=LocationStructure2(pos=Pos(value=[114311, 557575], srs_dimension=2)),
                              projections=ProjectionsRelStructure(choice=[PointProjection(id=getId(PointProjection, codespace, "DH-A-4"), version=version.version, project_to_point_ref=getRef(rp_tx, PointRefStructure))]),
                              for_alighting=True, for_boarding=False,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_tx)]),
                              private_code=PrivateCode(value="4", type_value="UserStopCode"))

scheduled_stop_points=[ssp_dh_1, ssp_dh_2, ssp_tx_1, ssp_tx_2]

tl_dhtx = TimingLink(id=getId(TimingLink, codespace, "DH-TX"), version=version.version,
                    from_point_ref=getRef(ssp_dh_1, TimingPointRefStructure), to_point_ref=getRef(ssp_tx_2, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_txdh = TimingLink(id=getId(TimingLink, codespace, "TX-DH"), version=version.version,
                    from_point_ref=getRef(ssp_tx_1, TimingPointRefStructure), to_point_ref=getRef(ssp_dh_2, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

timing_links = [tl_dhtx, tl_txdh]


# stop_assignments=[PassengerStopAssignment(), PassengerStopAssignment(), PassengerStopAssignment(), PassengerStopAssignment()]

sjp_dhtx = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "DH-TX"), version=version.version,
                                 route_ref_or_route_view=getRef(route_dhtx),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_tx),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "DH-TX-DH"), version=version.version, order=1,
                                                                   fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=getRef(ssp_dh_1),
                                                                   onward_timing_link_ref=getRef(tl_dhtx, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "DH-TX-TX"),
                                             version=version.version, order=2,
                                             fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=getRef(ssp_tx_2)),
                                     ]
                                    )
                                 )

sjp_txdh = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "TX-DH"), version=version.version,
                                 route_ref_or_route_view=getRef(route_txdh),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_dh),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "TX-DH-TX"), version=version.version, order=1,
                                                                   fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=getRef(ssp_tx_1),
                                                                   onward_timing_link_ref=getRef(tl_txdh, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "TX-DH-DH"),
                                             version=version.version, order=2,
                                             fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref=getRef(ssp_dh_2)),
                                     ]
                                    )
                                 )


journey_patterns=[sjp_dhtx, sjp_txdh]

tdt_dhtx = TimeDemandType(id=getId(TimeDemandType, codespace, "DH-TX"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "DH-TX"), version=version.version, timing_link_ref=getRef(tl_dhtx), run_time=XmlDuration("PT1200S"))]))

tdt_txdh = TimeDemandType(id=getId(TimeDemandType, codespace, "TX-DH"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "TX-DH"), version=version.version, timing_link_ref=getRef(tl_txdh), run_time=XmlDuration("PT1200S"))]))

time_demand_types=[tdt_dhtx, tdt_txdh]

service_frames = dutchprofile.getServiceFrames(route_points=route_points, route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=scheduled_stop_points, stop_areas=stop_areas,
                                              stop_assignments=None, timing_points=None, timing_links=timing_links, service_journey_patterns=journey_patterns, time_demand_types=None,
                                              notices=None, notice_assignments=None)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[codespace], resource_frames=resource_frames, service_frames=service_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste TESO export")

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(serializer_config)

with open('netex-output/out.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)