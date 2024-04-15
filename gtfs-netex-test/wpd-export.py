from _decimal import Decimal
from pathlib import Path
from typing import Dict, List

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import lxml, LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from availabilityconditionsprofile import AvailabilityConditionsProfile
from dutchprofile import DutchProfile
from netex import PublicationDelivery, GeneralFrame, Codespace, DataSource, TransportAdministrativeZone, \
    MultilingualString, AllModesEnumeration, Operator, Authority, ResponsibilitySet, \
    ResponsibilityRoleAssignmentsRelStructure, ResponsibilityRoleAssignment, TypeOfResponsibilityRoleRef, \
    OrganisationRefStructure, VersionOfObjectRefStructure, OperationalContext, AllVehicleModesOfTransportEnumeration, \
    FuelTypeEnumeration, VehicleType, PassengerCapacitiesRelStructure, PassengerCapacity, FareClassEnumeration, \
    ServiceFacilitySetsRelStructure, ServiceFacilitySet, MobilityFacilityEnumeration, PassengerCommsFacilityEnumeration, \
    SanitaryFacilityEnumeration, MealFacilityEnumeration, AssistanceFacilityEnumeration, \
    VehicleAccessFacilityEnumeration, Line, TypeOfServiceRef, PrivateCode, AccessibilityAssessment, \
    LimitationStatusEnumeration, RoutePoint, LocationStructure2, Pos, RouteLink, RoutePointRefStructure, LineString, \
    PosList, Route, DirectionTypeEnumeration, PointsOnRouteRelStructure, PointOnRoute, RouteLinkRefStructure, \
    DestinationDisplay, DestinationDisplayVariantsRelStructure, DestinationDisplayVariant, StopArea, \
    TopographicPlaceView, ScheduledStopPoint, StopAreaRefsRelStructure, PassengerStopAssignment, QuayRef, OperatorView, \
    Version, ServiceJourney, VehicleTypeRef, ServiceJourneyPattern, RouteRef, DeliveryVariantTypeEnumeration, \
    Extensions2, StopPointInJourneyPattern, DestinationDisplayRef, ProjectionsRelStructure, PointProjection, \
    PointRefStructure, DirectionType, TransportTypeVersionStructure
from refs import getId, getRef, getFakeRef
from timedemandtypesprofile import TimeDemandTypesProfile

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

publication_delivery = parser.from_path(Path("netex-output/wpd-raw.xml"), PublicationDelivery)

general_frame: GeneralFrame = publication_delivery.data_objects.choice[0]
codespace: Codespace = general_frame.codespaces.codespace_ref_or_codespace[0]
version: Version = general_frame.versions.version_ref_or_version[0]

short_name = "WPD"

dova_codespace = Codespace(id="{}:Codespace:{}".format("BISON", "DOVA"), xmlns="DOVA",
                      xmlns_url="http://bison.dova.nu/ns/DOVA", description=MultilingualString(value="'Centrale' lijsten bijgehouden door DOVA"))

data_source = [x for x in general_frame.members.choice if isinstance(x, DataSource)][0]

operator = [x for x in general_frame.members.choice if isinstance(x, Operator)][0]

ssps: Dict[str, ScheduledStopPoint] = {x.name.value[0] : x for x in general_frame.members.choice if isinstance(x, ScheduledStopPoint)}

transport_administrative_zone = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "WPD"),
                                                            version="any",
                                                            name=MultilingualString(value="Waddenveren Oost"),
                                                            short_name=MultilingualString(value="WPD"),
                                                            vehicle_modes=[AllModesEnumeration.FERRY])


authority = Authority(id=getId(Authority, codespace, "Rijk"), version="any", name=MultilingualString(value="Rijksoverheid"), short_name=MultilingualString(value="RIJK"), description=MultilingualString(value="Rijksoverheid"))

responsibility_set = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, short_name),
                                       version=version.version,
                                       name=MultilingualString(value=short_name),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(
                                               id=getId(ResponsibilityRoleAssignment, codespace, "RIJK"),
                                               version=version.version,
                                               data_role_type=None,
                                               stakeholder_role_type=None,
                                               type_of_responsibility_role_ref_or_responsibility_role_ref=TypeOfResponsibilityRoleRef(ref="BISON:TypeOfResponsibilityRole:financing", version="any"),
                                               responsible_organisation_ref=getRef(authority, OrganisationRefStructure)),
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "WPD"),
                                                                        version=version.version,
                                                                        data_role_type=None,
                                                                        stakeholder_role_type=None,
                                                                        responsible_area_ref=getRef(transport_administrative_zone, VersionOfObjectRefStructure))
                                       ]))


operational_context = OperationalContext(id=getId(OperationalContext, codespace, "WATER"), version=version.version,
                                       name=MultilingualString(value="WATER"), short_name=MultilingualString(value="WATER"),
                                         vehicle_mode=AllVehicleModesOfTransportEnumeration.FERRY)



vehicle_type_vieroerd = VehicleType(id=getId(VehicleType, codespace, "SIEROERD"), version=version.version,
                           name=MultilingualString(value="Sier en Oerd"),
                           description=MultilingualString(value="Sier en Oerd"),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity=
                                                                      [PassengerCapacity(id=getId(PassengerCapacity, codespace, "SIEROERD"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=1200)]),
                           length=Decimal(value='73.20'), width=Decimal(value='15.90'), height=Decimal(value='5.65'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "SIEROERD"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET,
                                                                           SanitaryFacilityEnumeration.BABY_CHANGE],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

vehicle_type_rottummonnik = VehicleType(id=getId(VehicleType, codespace, "ROTTUMMONNIK"), version=version.version,
                           name=MultilingualString(value="Rottum en Monnik"),
                           description=MultilingualString(value="Rottum en Monnik"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "ROTTUMMONNIK"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=1000)),
                           length=Decimal(value='58'), width=Decimal(value='13.82'), height=Decimal(value='5.45'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "ROTTUMMONNIK"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET,
                                                                           SanitaryFacilityEnumeration.BABY_CHANGE],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

vehicle_type_fostaborg = VehicleType(id=getId(VehicleType, codespace, "FOSTABORG"), version=version.version,
                           name=MultilingualString(value="Fostaborg"),
                           description=MultilingualString(value="Fostaborg"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "FOSTABORG"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=48)),
                           length=Decimal(value='21.5'), width=Decimal(value='7.00'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "FOSTABORG"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

vehicle_type_esonborg = VehicleType(id=getId(VehicleType, codespace, "ESONBORG"), version=version.version,
                           name=MultilingualString(value="Esonborg"),
                           description=MultilingualString(value="Esonborg"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "ESONBORG"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=48)),
                           length=Decimal(value='22'), width=Decimal(value='6.10'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "ESONBORG"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))


dutchprofile = DutchProfile(codespace, data_source, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set],
                                                 organisations=[operator, authority], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type_rottummonnik,
                                                                vehicle_type_vieroerd,
                                                                vehicle_type_esonborg,
                                                                vehicle_type_fostaborg], zones=[transport_administrative_zone])

line_ha = Line(id=getId(Line, codespace, "HA"), version=version.version, name=MultilingualString(value="Holwerd - Ameland"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Holwerd en Ameland"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="HA",
              private_code=PrivateCode(value="1", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "HA"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_shsa = Line(id=getId(Line, codespace, "SHSA"), version=version.version, name=MultilingualString(value="Holwerd - Ameland (Sneldienst)"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Holwerd en Ameland (Sneldienst)"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="SHSA",
              private_code=PrivateCode(value="2", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "SHSA"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_ls = Line(id=getId(Line, codespace, "LS"), version=version.version, name=MultilingualString(value="Lauwersoog - Schiermonnikoog"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Lauwersoog en Schiermonnikoog"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="LS",
              private_code=PrivateCode(value="3", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "LS"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_slss = Line(id=getId(Line, codespace, "SLSS"), version=version.version, name=MultilingualString(value="Lauwersoog - Schiermonnikoog (Sneldienst)"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Lauwersoog en Schiermonnikoog (Sneldienst)"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="SLSS",
              private_code=PrivateCode(value="4", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "SLSS"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

lines = [line_ha, line_shsa, line_ls, line_slss]


rp_h = RoutePoint(id=getId(RoutePoint, codespace, "HO"), version=version.version, location=LocationStructure2(pos=Pos(value=[187721, 601113], srs_dimension=2)))
rp_a = RoutePoint(id=getId(RoutePoint, codespace, "AM"), version=version.version, location=LocationStructure2(pos=Pos(value=[180750, 605311], srs_dimension=2)))
rp_l = RoutePoint(id=getId(RoutePoint, codespace, "LA"), version=version.version, location=LocationStructure2(pos=Pos(value=[208889, 603004], srs_dimension=2)))
rp_s = RoutePoint(id=getId(RoutePoint, codespace, "SC"), version=version.version, location=LocationStructure2(pos=Pos(value=[203187, 609466], srs_dimension=2)))

route_points = {x.id : x for x in [rp_h, rp_a, rp_l, rp_s]}

rl_ha = RouteLink(id=getId(RouteLink, codespace, "H-A"), version=version.version,
                  distance=Decimal('17000'),
                  from_point_ref=getRef(rp_h, RoutePointRefStructure), to_point_ref=getRef(rp_a, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "H-A").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_h.location.pos.value + rp_a.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_ah = RouteLink(id=getId(RouteLink, codespace, "A-H"), version=version.version,
                  distance=Decimal('17000'),
                  from_point_ref=getRef(rp_a, RoutePointRefStructure), to_point_ref=getRef(rp_h, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "A-H").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_a.location.pos.value + rp_h.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_ls = RouteLink(id=getId(RouteLink, codespace, "L-S"), version=version.version,
                  distance=Decimal('12000'),
                  from_point_ref=getRef(rp_l, RoutePointRefStructure), to_point_ref=getRef(rp_s, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "L-S").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_l.location.pos.value + rp_s.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_sl = RouteLink(id=getId(RouteLink, codespace, "S-L"), version=version.version,
                  distance=Decimal('12000'),
                  from_point_ref=getRef(rp_s, RoutePointRefStructure), to_point_ref=getRef(rp_l, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "S-L").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_l.location.pos.value + rp_s.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_ha, rl_ah, rl_ls, rl_sl]

route_hoam = Route(id=getId(Route, codespace, "HOAM"), version=version.version,
                 distance=Decimal('17000'),
                 line_ref=getRef(line_ha),
                   direction_type=DirectionType(DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "HOAM-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h), onward_route_link_ref=getRef(rl_ha, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "HOAM-A"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a)),
                   ])
                   )

route_amho = Route(id=getId(Route, codespace, "AMHO"), version=version.version,
                 distance=Decimal('17000'),
                 line_ref=getRef(line_ha),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "AMHO-A"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a), onward_route_link_ref=getRef(rl_ah, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "AMHO-H"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h)),
                   ])
                   )

route_lasc = Route(id=getId(Route, codespace, "LASC"), version=version.version,
                 distance=Decimal('12000'),
                 line_ref=getRef(line_ls),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LASC-L"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l), onward_route_link_ref=getRef(rl_ls, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LASC-S"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s)),
                   ])
                   )

route_scla = Route(id=getId(Route, codespace, "SCLA"), version=version.version,
                 distance=Decimal('12000'),
                 line_ref=getRef(line_ls),
                   direction_type=DirectionTypeEnumeration.INBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SCLA-S"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s), onward_route_link_ref=getRef(rl_sl, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SCLA-L"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l)),
                   ])
                   )

route_shsa = Route(id=getId(Route, codespace, "SHSA"), version=version.version,
                 distance=Decimal('17000'),
                 line_ref=getRef(line_shsa),
                   direction_type=DirectionTypeEnumeration.OUTBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SHSA-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h), onward_route_link_ref=getRef(rl_ha, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SHSA-A"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a)),
                   ])
                   )

route_sash = Route(id=getId(Route, codespace, "SASH"), version=version.version,
                 distance=Decimal('17000'),
                 line_ref=getRef(line_shsa),
                   direction_type=DirectionTypeEnumeration.INBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SASH-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a), onward_route_link_ref=getRef(rl_ah, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SASH-A"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h)),
                   ])
                   )

route_slss = Route(id=getId(Route, codespace, "SLSS"), version=version.version,
                 distance=Decimal('12000'),
                 line_ref=getRef(line_slss),
                   direction_type=DirectionTypeEnumeration.OUTBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SLSS-L"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l), onward_route_link_ref=getRef(rl_ls, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SLSS-S"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s)),
                   ])
                   )

route_sssl = Route(id=getId(Route, codespace, "SSSL"), version=version.version,
                 distance=Decimal('12000'),
                 line_ref=getRef(line_slss),
                   direction_type=DirectionTypeEnumeration.INBOUND,
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SSSL-S"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s), onward_route_link_ref=getRef(rl_sl, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SSSL-L"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l)),
                   ])
                   )

routes = [route_hoam, route_amho, route_lasc, route_scla, route_sash, route_shsa, route_slss, route_sssl]



sa_h = StopArea(id=getId(StopArea, codespace, "HO"),
                 version=version.version,
                 name=MultilingualString(value="Holwerd"),
                 private_code=PrivateCode(value="1", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Harlingen"))
                 )

sa_a = StopArea(id=getId(StopArea, codespace, "AM"),
                 version=version.version,
                 name=MultilingualString(value="Ameland"),
                 private_code=PrivateCode(value="2", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Terschelling"))
                 )

sa_l = StopArea(id=getId(StopArea, codespace, "LA"),
                 version=version.version,
                 name=MultilingualString(value="Laurensoog"),
                 private_code=PrivateCode(value="3", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Vlieland"))
                 )

sa_s = StopArea(id=getId(StopArea, codespace, "SC"),
                 version=version.version,
                 name=MultilingualString(value="Schiermonnikoog"),
                 private_code=PrivateCode(value="4", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Vlieland"))
                 )

stop_areas=[sa_h, sa_a, sa_l, sa_s]

ssps['H'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_h)])
ssps['H'].private_code=PrivateCode(value="20650001", type_value="UserStopCode")
ssps['A'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_a)])
ssps['A'].private_code=PrivateCode(value="29190001", type_value="UserStopCode")
ssps['L'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_l)])
ssps['L'].private_code=PrivateCode(value="10380001", type_value="UserStopCode")
ssps['S'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_s)])
ssps['S'].private_code=PrivateCode(value="29310001", type_value="UserStopCode")

for ssp in ssps.values():
    rp: RoutePoint = route_points[ssp.id.replace('ScheduledStopPoint', 'RoutePoint')]
    ssp.location = rp.location
    ssp.projections = ProjectionsRelStructure(projection_ref_or_projection=[
        PointProjection(id=ssp.id.replace('ScheduledStopPoint', 'PointProjection'), version=version.version,
                        project_to_point_ref=getRef(rp, PointRefStructure))])

stop_assignments=[PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "H"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssps['H']),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:20650001", QuayRef, "any")),

                PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "A"), version=version.version, order=1,
                                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssps['A']),
                                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:29190001", QuayRef, "any")),

                PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "L"), version=version.version, order=1,
                                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssps['L']),
                                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:10380001", QuayRef, "any")),

                PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "S"), version=version.version, order=1,
                                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssps['S']),
                                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:29310001", QuayRef, "any")),
]

ssps: Dict[str, ScheduledStopPoint] = {x.id: x for x in general_frame.members.choice if
                                       isinstance(x, ScheduledStopPoint)}
sjs: List[ServiceJourney] = [x for x in general_frame.members.choice if isinstance(x, ServiceJourney)]
sjps = {}
sjps_hash = {}
tls = {}
tdts = {}
tdts_hash = {}

tdtp = TimeDemandTypesProfile(codespace=codespace, version=version)

for sj in sjs:
    tdtp.getServiceJourneyPattern(sj, sjps, sjps_hash, ssps, tls)
    tdtp.getTimeDemandType(sj, sjps, tdts, tdts_hash, ssps, tls, None)
    sj.private_code = PrivateCode(type_value="JourneyNumber", value=str(int(str(sj.departure_time).replace(':', ''))))
    if sj.journey_pattern_ref.ref in ('WPD:ServiceJourneyPattern:AMHO', 'WPD:ServiceJourneyPattern:HOAM'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_vieroerd, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('WPD:ServiceJourneyPattern:LASC', 'WPD:ServiceJourneyPattern:SCLA'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_rottummonnik, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('WPD:ServiceJourneyPattern:SASH', 'WPD:ServiceJourneyPattern:SHSA'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_fostaborg, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('WPD:ServiceJourneyPattern:SLSS', 'WPD:ServiceJourneyPattern:SSSL'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_esonborg, VehicleTypeRef)

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_ho = DestinationDisplay(id=getId(DestinationDisplay, codespace, "HO"), version=version.version,
                           name=MultilingualString(value="Holwerd"),
                           front_text=MultilingualString(value="Holwerd"),
                           private_code=PrivateCode(value="1", type_value="DestinationCode"))
setVariants(dd_ho)

dd_am = DestinationDisplay(id=getId(DestinationDisplay, codespace, "AM"), version=version.version,
                           name=MultilingualString(value="Ameland"),
                           front_text=MultilingualString(value="Ameland"),
                           private_code=PrivateCode(value="2", type_value="DestinationCode"))
setVariants(dd_am)

dd_la = DestinationDisplay(id=getId(DestinationDisplay, codespace, "LA"), version=version.version,
                           name=MultilingualString(value="Laurersoog"),
                           front_text=MultilingualString(value="Laurersoog"),
                           private_code=PrivateCode(value="3", type_value="DestinationCode"))
setVariants(dd_la)

dd_sc = DestinationDisplay(id=getId(DestinationDisplay, codespace, "SC"), version=version.version,
                           name=MultilingualString(value="Schiermonnikoog"),
                           front_text=MultilingualString(value="Schiermonnikoog"),
                           private_code=PrivateCode(value="4", type_value="DestinationCode"))
setVariants(dd_sc)

destination_displays=[dd_ho, dd_am, dd_la, dd_sc]

sjp: ServiceJourneyPattern
for sjp in sjps.values():
    sjp.route_ref_or_route_view = getFakeRef(sjp.id.replace("ServiceJourneyPattern", "Route"), RouteRef, version.version)
    spijp: StopPointInJourneyPattern = sjp.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern[-1]
    sjp.destination_display_ref_or_destination_display_view = getFakeRef(spijp.scheduled_stop_point_ref.ref.replace('ScheduledStopPoint', 'DestinationDisplay'), DestinationDisplayRef, version.version)

acp = AvailabilityConditionsProfile(codespace=codespace, version=version)
service_journeys, availability_conditions = acp.deduplicate(sjs)

for ac in availability_conditions:
    if version.start_date.to_datetime() > ac.from_date.to_datetime():
        version.start_date = ac.from_date.to
    if version.end_date.to_datetime() < ac.to_date.to_datetime():
        version.end_date = ac.to_date

service_frames = dutchprofile.getServiceFrames(route_points=list(route_points.values()), route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=list(ssps.values()), stop_areas=stop_areas,
                                              stop_assignments=stop_assignments, timing_points=None, timing_links=list(tls.values()),
                                               service_journey_patterns=list(sjps.values()), time_demand_types=list(tdts.values()),
                                              notices=None, notice_assignments=None)

timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions, operator_view=OperatorView(operator_ref=getRef(operator)), vehicle_journeys=service_journeys)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[dova_codespace, codespace], versions=[version],
                                                 responsibility_set=responsibility_set,
                                                 resource_frames=resource_frames, service_frames=service_frames, timetable_frames=timetable_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste WPD export")

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

with open('netex-output/wpd.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)

parser = lxml.etree.XMLParser(remove_blank_text=True)
tree = lxml.etree.parse("netex-output/wpd.xml", parser=parser)
for element in tree.iterfind(".//*"):
    if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
        element.getparent().remove(element)
tree.write("netex-output/wpd-filter.xml", pretty_print=True, strip_text=True)
