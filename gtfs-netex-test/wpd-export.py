from _decimal import Decimal
import datetime
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
    PointRefStructure, DirectionType, TransportTypeVersionStructure, MobilityFacilityList, PassengerCommsFacilityList, \
    SanitaryFacilityList, MealFacilityList, AssistanceFacilityList, VehicleAccessFacilityList, PublicCodeStructure, \
    DatedServiceJourney, TimingLink, ValidBetween, PrivateCodes, Notice, NoticeAssignment, OperatorRefStructure, VersionOfObjectRefStructure
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
valid_between: ValidBetween = ValidBetween(from_date=version.start_date, to_date=version.end_date)

short_name = "WPD"
xmlns = "NL:WPD"

dova_codespace = Codespace(id="{}:Codespace:{}".format("BISON", "DOVA"), xmlns="NL:DOVA",
                      xmlns_url="http://bison.dova.nu/ns/DOVA", description=MultilingualString(value="'Centrale' lijsten bijgehouden door DOVA"))

data_source = [x for x in general_frame.members.choice if isinstance(x, DataSource)][0]

operator = [x for x in general_frame.members.choice if isinstance(x, Operator)][0]

ssps: Dict[str, ScheduledStopPoint] = {x.name.value[0] : x for x in general_frame.members.choice if isinstance(x, ScheduledStopPoint)}

transport_administrative_zone = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "WPD"),
                                                            version="any",
                                                            name=MultilingualString(value="Waddenveren Oost"),
                                                            short_name=MultilingualString(value="WPD"),
                                                            vehicle_modes=[AllModesEnumeration.WATER])


# authority = Authority(id=getId(Authority, codespace, "Rijk"), version="any", name=MultilingualString(value="Rijksoverheid"), short_name=MultilingualString(value="RIJK"), description=MultilingualString(value="Rijksoverheid"))

transport_administrative_zone_partitie = transport_administrative_zone

responsibility_set_financier = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, "Financier"),
                                       version=version.version,
                                       name=MultilingualString(value="Financier"),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(
                                               id=getId(ResponsibilityRoleAssignment, codespace, "Financier"),
                                               version=version.version,
                                               type_of_responsibility_role_ref_or_responsibility_role_ref=TypeOfResponsibilityRoleRef(ref="BISON:TypeOfResponsibilityRole:financing", version="any"),
                                               responsible_organisation_ref=getRef(operator, OrganisationRefStructure)),
                                       ]))

responsibility_set_partitie = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, xmlns),
                                       version=version.version,
                                       name=MultilingualString(value="Partitie"),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "Partitie"),
                                                                        version=version.version,
                                                                        responsible_area_ref=getRef(transport_administrative_zone_partitie, VersionOfObjectRefStructure))
                                       ]))


operational_context = OperationalContext(id=getId(OperationalContext, codespace, "WATER"), version=version.version,
                                       name=MultilingualString(value="WATER"), short_name=MultilingualString(value="WATER"),
                                         vehicle_mode=AllVehicleModesOfTransportEnumeration.WATER)



vehicle_type_vieroerd = VehicleType(id=getId(VehicleType, codespace, "SIEROERD"), version=version.version,
                           name=MultilingualString(value="Sier en Oerd"),
                           description=MultilingualString(value="Sier en Oerd"),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      [PassengerCapacity(id=getId(PassengerCapacity, codespace, "SIEROERD"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=1200)]),
                           length=Decimal(value='73.20'), width=Decimal(value='15.90'), height=Decimal(value='5.65'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               restricted_service_facility_set_ref_or_service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "SIEROERD"), version=version.version,
                                                   mobility_facility_list=MobilityFacilityList(value=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                                                   passenger_comms_facility_list=PassengerCommsFacilityList(value=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI]),
                                                   sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET,
                                                                           SanitaryFacilityEnumeration.BABY_CHANGE]),
                                                   meal_facility_list=MealFacilityList(value=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS]),
                                                   assistance_facility_list=AssistanceFacilityList(value=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP])
                           )]))

vehicle_type_rottummonnik = VehicleType(id=getId(VehicleType, codespace, "ROTTUMMONNIK"), version=version.version,
                           name=MultilingualString(value="Rottum en Monnik"),
                           description=MultilingualString(value="Rottum en Monnik"),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      [PassengerCapacity(id=getId(PassengerCapacity, codespace, "ROTTUMMONNIK"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=1000)]),
                           length=Decimal(value='58'), width=Decimal(value='13.82'), height=Decimal(value='5.45'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               restricted_service_facility_set_ref_or_service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "ROTTUMMONNIK"), version=version.version,
                                                   mobility_facility_list=MobilityFacilityList(value=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                                                   passenger_comms_facility_list=PassengerCommsFacilityList(value=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI]),
                                                   sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET,
                                                                           SanitaryFacilityEnumeration.BABY_CHANGE]),
                                                   meal_facility_list=MealFacilityList(value=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS]),
                                                   assistance_facility_list=AssistanceFacilityList(value=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP])
                           )]))

vehicle_type_fostaborg = VehicleType(id=getId(VehicleType, codespace, "FOSTABORG"), version=version.version,
                           name=MultilingualString(value="Fostaborg"),
                           description=MultilingualString(value="Fostaborg"),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=[
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "FOSTABORG"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=48)]),
                           length=Decimal(value='21.5'), width=Decimal(value='7.00'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               restricted_service_facility_set_ref_or_service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "FOSTABORG"), version=version.version,
                                                   mobility_facility_list=MobilityFacilityList(value=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                                                   passenger_comms_facility_list=PassengerCommsFacilityList(value=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI]),
                                                   sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET]),
                                                   assistance_facility_list=AssistanceFacilityList(value=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP])
                           )]))

vehicle_type_esonborg = VehicleType(id=getId(VehicleType, codespace, "ESONBORG"), version=version.version,
                           name=MultilingualString(value="Esonborg"),
                           description=MultilingualString(value="Esonborg"),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=[
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "ESONBORG"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=48)]),
                           length=Decimal(value='22'), width=Decimal(value='6.10'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=True,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               restricted_service_facility_set_ref_or_service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "ESONBORG"), version=version.version,
                                                   mobility_facility_list=MobilityFacilityList(value=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                                                   passenger_comms_facility_list=PassengerCommsFacilityList(value=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI]),
                                                   sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET]),
                                                   assistance_facility_list=AssistanceFacilityList(value=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP])
                           )]))


dutchprofile = DutchProfile(codespace, data_source, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set_partitie, responsibility_set_financier],
                                                 organisations=[operator], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type_rottummonnik,
                                                                vehicle_type_vieroerd,
                                                                vehicle_type_esonborg,
                                                                vehicle_type_fostaborg], zones=[transport_administrative_zone])

line_ha = Line(id=getId(Line, codespace, "HA"), version=version.version, name=MultilingualString(value="Holwerd - Ameland"),
              monitored=False,
               operator_ref=getRef(operator),
               responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Veer tussen Holwerd en Ameland"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="HA"),
              private_codes=PrivateCodes(private_code=[PrivateCode(value="1", type_value="LinePlanningNumber")]),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "HA"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_shsa = Line(id=getId(Line, codespace, "SHSA"), version=version.version, name=MultilingualString(value="Holwerd - Ameland (Sneldienst)"),
              monitored=False,
                 operator_ref=getRef(operator),

                 responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Veer tussen Holwerd en Ameland (Sneldienst)"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="SHSA"),
              private_codes=PrivateCodes(private_code=[PrivateCode(value="2", type_value="LinePlanningNumber")]),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "SHSA"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_ls = Line(id=getId(Line, codespace, "LS"), version=version.version, name=MultilingualString(value="Lauwersoog - Schiermonnikoog"),
              monitored=False,
               operator_ref=getRef(operator),

               responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Veer tussen Lauwersoog en Schiermonnikoog"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="LS"),
              private_codes=PrivateCodes(private_code=[PrivateCode(value="3", type_value="LinePlanningNumber")]),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "LS"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_slss = Line(id=getId(Line, codespace, "SLSS"), version=version.version, name=MultilingualString(value="Lauwersoog - Schiermonnikoog (Sneldienst)"),
              monitored=False,
                 operator_ref=getRef(operator),
                 responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Veer tussen Lauwersoog en Schiermonnikoog (Sneldienst)"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="SLSS"),
              private_codes=PrivateCodes(private_code=[PrivateCode(value="4", type_value="LinePlanningNumber")]),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "SLSS"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

lines = [line_ha, line_shsa, line_ls, line_slss]


rp_h = RoutePoint(id=getId(RoutePoint, codespace, "HO"), version=version.version, location=LocationStructure2(pos=Pos(value=[187721.0, 601111.9], srs_dimension=2)))
rp_a = RoutePoint(id=getId(RoutePoint, codespace, "AM"), version=version.version, location=LocationStructure2(pos=Pos(value=[180751.3, 605310.2], srs_dimension=2)))
rp_l = RoutePoint(id=getId(RoutePoint, codespace, "LA"), version=version.version, location=LocationStructure2(pos=Pos(value=[208949.5, 603001.4], srs_dimension=2)))
rp_s = RoutePoint(id=getId(RoutePoint, codespace, "SC"), version=version.version, location=LocationStructure2(pos=Pos(value=[209190.6, 609466.6], srs_dimension=2)))

route_points = {x.id : x for x in [rp_h, rp_a, rp_l, rp_s]}

rl_ha = RouteLink(id=getId(RouteLink, codespace, "H-A"), version=version.version,
                  distance=Decimal('12179'),
                  from_point_ref=getRef(rp_h, RoutePointRefStructure), to_point_ref=getRef(rp_a, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "H-A").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=[187721.0, 601111.9, 187664.4, 601162.7, 187631.0, 601180.7, 187598.1, 601182.5, 187571.6, 601178.8, 187434.1, 601137.5, 187187.5, 601035.4, 186751.9, 600839.4, 186468.6, 600748.8, 186247.4, 600725.7, 186064.7, 600742.8, 185893.6, 600798.8, 185767.0, 600880.7, 185667.5, 600972.2, 185546.6, 601103.4, 185446.6, 601266.3, 185378.4, 601439.3, 185349.3, 601571.1, 185342.7, 601675.4, 185337.1, 601736.5, 185324.2, 601807.3, 185300.3, 601864.3, 185194.7, 601995.7, 185030.0, 602171.9, 184938.9, 602239.8, 184840.9, 602283.1, 184740.6, 602322.3, 184639.2, 602335.0, 184460.3, 602337.8, 184262.7, 602293.3, 184120.7, 602233.8, 184011.6, 602159.7, 183698.5, 601953.0, 183596.5, 601878.0, 183493.5, 601778.8, 183367.1, 601653.5, 183209.8, 601567.8, 183058.1, 601535.4, 182895.5, 601542.3, 182762.3, 601573.6, 182643.2, 601609.8, 182536.9, 601658.5, 182477.7, 601725.1, 182446.8, 601760.9, 182428.8, 601817.4, 182420.1, 601904.6, 182444.2, 602019.0, 182469.6, 602105.8, 182504.2, 602220.3, 182529.4, 602348.5, 182560.0, 602559.5, 182573.0, 602750.2, 182574.7, 602857.1, 182568.9, 602957.0, 182507.9, 603217.2, 182437.1, 603455.2, 182351.7, 603672.9, 182238.3, 603842.2, 182145.9, 603961.9, 182044.6, 604079.0, 181945.3, 604151.4, 181834.5, 604182.3, 181733.3, 604181.7, 181106.3, 604127.0, 180980.3, 604148.0, 180843.3, 604237.9, 180774.6, 604328.1, 180706.8, 604449.9, 180627.4, 604557.8, 180534.0, 604640.1, 180449.1, 604679.0, 180339.5, 604704.1, 180213.3, 604748.7, 180160.2, 604791.8, 180132.7, 604860.6, 180138.2, 604947.3, 180169.5, 605022.4, 180237.4, 605089.7, 180388.9, 605141.7, 180578.3, 605158.5, 180670.6, 605163.4, 180708.2, 605183.3, 180737.4, 605222.4, 180751.3, 605310.2])]),
                    operational_context_ref=getRef(operational_context))

rl_ah = RouteLink(id=getId(RouteLink, codespace, "A-H"), version=version.version,
                  distance=Decimal('12179'),
                  from_point_ref=getRef(rp_a, RoutePointRefStructure), to_point_ref=getRef(rp_h, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "A-H").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=[180751.3, 605310.2, 180737.4, 605222.4, 180708.2, 605183.3, 180670.6, 605163.4, 180578.3, 605158.5, 180388.9, 605141.7, 180237.4, 605089.7, 180169.5, 605022.4, 180138.2, 604947.3, 180132.7, 604860.6, 180160.2, 604791.8, 180213.3, 604748.7, 180339.5, 604704.1, 180449.1, 604679.0, 180534.0, 604640.1, 180627.4, 604557.8, 180706.8, 604449.9, 180774.6, 604328.1, 180843.3, 604237.9, 180980.3, 604148.0, 181106.3, 604127.0, 181733.3, 604181.7, 181834.5, 604182.3, 181945.3, 604151.4, 182044.6, 604079.0, 182145.9, 603961.9, 182238.3, 603842.2, 182351.7, 603672.9, 182437.1, 603455.2, 182507.9, 603217.2, 182568.9, 602957.0, 182574.7, 602857.1, 182573.0, 602750.2, 182560.0, 602559.5, 182529.4, 602348.5, 182504.2, 602220.3, 182469.6, 602105.8, 182444.2, 602019.0, 182420.1, 601904.6, 182428.8, 601817.4, 182446.8, 601760.9, 182477.7, 601725.1, 182536.9, 601658.5, 182643.2, 601609.8, 182762.3, 601573.6, 182895.5, 601542.3, 183058.1, 601535.4, 183209.8, 601567.8, 183367.1, 601653.5, 183493.5, 601778.8, 183596.5, 601878.0, 183698.5, 601953.0, 184011.6, 602159.7, 184120.7, 602233.8, 184262.7, 602293.3, 184460.3, 602337.8, 184639.2, 602335.0, 184740.6, 602322.3, 184840.9, 602283.1, 184938.9, 602239.8, 185030.0, 602171.9, 185194.7, 601995.7, 185300.3, 601864.3, 185324.2, 601807.3, 185337.1, 601736.5, 185342.7, 601675.4, 185349.3, 601571.1, 185378.4, 601439.3, 185446.6, 601266.3, 185546.6, 601103.4, 185667.5, 600972.2, 185767.0, 600880.7, 185893.6, 600798.8, 186064.7, 600742.8, 186247.4, 600725.7, 186468.6, 600748.8, 186751.9, 600839.4, 187187.5, 601035.4, 187434.1, 601137.5, 187571.6, 601178.8, 187598.1, 601182.5, 187631.0, 601180.7, 187664.4, 601162.7, 187721.0, 601111.9])]),
                    operational_context_ref=getRef(operational_context))

rl_ls = RouteLink(id=getId(RouteLink, codespace, "L-S"), version=version.version,
                  distance=Decimal('11253'),
                  from_point_ref=getRef(rp_l, RoutePointRefStructure), to_point_ref=getRef(rp_s, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "L-S").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=[209190.6, 609466.6, 209217.1, 609470.7, 209230.2, 609465.6, 209231.0, 609448.5, 209172.8, 609406.3, 208833.3, 609185.1, 208745.6, 609102.6, 208647.6, 608969.8, 208582.6, 608920.8, 208423.9, 608859.8, 208166.2, 608768.8, 208064.4, 608719.3, 207992.8, 608672.6, 207899.4, 608587.0, 207824.8, 608486.0, 207720.5, 608331.4, 207551.1, 608005.8, 207441.0, 607787.2, 207348.7, 607532.6, 207310.4, 607468.1, 207260.7, 607399.9, 206506.9, 606900.2, 206166.8, 606741.9, 205593.5, 606604.2, 205222.1, 606535.0, 205117.0, 606521.8, 205069.8, 606482.7, 205044.7, 606400.3, 205053.0, 606296.5, 205134.3, 606111.4, 205243.7, 605861.3, 205383.7, 605577.7, 205518.1, 605417.3, 205689.8, 605281.4, 208637.8, 603801.4, 208899.5, 603635.2, 209036.7, 603491.8, 209125.6, 603289.9, 209115.7, 603147.3, 209068.2, 603067.0, 209015.2, 603022.7, 208988.1, 603010.0, 208972.8, 603001.9, 208949.5, 603001.4])]),
                    operational_context_ref=getRef(operational_context))

rl_sl = RouteLink(id=getId(RouteLink, codespace, "S-L"), version=version.version,
                  distance=Decimal('11253'),
                  from_point_ref=getRef(rp_s, RoutePointRefStructure), to_point_ref=getRef(rp_l, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "S-L").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=[208949.5, 603001.4, 208972.8, 603001.9, 208988.1, 603010.0, 209015.2, 603022.7, 209068.2, 603067.0, 209115.7, 603147.3, 209125.6, 603289.9, 209036.7, 603491.8, 208899.5, 603635.2, 208637.8, 603801.4, 205689.8, 605281.4, 205518.1, 605417.3, 205383.7, 605577.7, 205243.7, 605861.3, 205134.3, 606111.4, 205053.0, 606296.5, 205044.7, 606400.3, 205069.8, 606482.7, 205117.0, 606521.8, 205222.1, 606535.0, 205593.5, 606604.2, 206166.8, 606741.9, 206506.9, 606900.2, 207260.7, 607399.9, 207310.4, 607468.1, 207348.7, 607532.6, 207441.0, 607787.2, 207551.1, 608005.8, 207720.5, 608331.4, 207824.8, 608486.0, 207899.4, 608587.0, 207992.8, 608672.6, 208064.4, 608719.3, 208166.2, 608768.8, 208423.9, 608859.8, 208582.6, 608920.8, 208647.6, 608969.8, 208745.6, 609102.6, 208833.3, 609185.1, 209172.8, 609406.3, 209231.0, 609448.5, 209230.2, 609465.6, 209217.1, 609470.7, 209190.6, 609466.6])]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_ha, rl_ah, rl_ls, rl_sl]

route_hoam = Route(id=getId(Route, codespace, "HOAM"), version=version.version,
                 distance=Decimal('12179'),
                 line_ref=getRef(line_ha),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "HOAM-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h), onward_route_link_ref=getRef(rl_ha, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "HOAM-A"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a)),
                   ])
                   )

route_amho = Route(id=getId(Route, codespace, "AMHO"), version=version.version,
                 distance=Decimal('12179'),
                 line_ref=getRef(line_ha),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "AMHO-A"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a), onward_route_link_ref=getRef(rl_ah, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "AMHO-H"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h)),
                   ])
                   )

route_lasc = Route(id=getId(Route, codespace, "LASC"), version=version.version,
                 distance=Decimal('11253'),
                 line_ref=getRef(line_ls),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LASC-L"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l), onward_route_link_ref=getRef(rl_ls, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LASC-S"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s)),
                   ])
                   )

route_scla = Route(id=getId(Route, codespace, "SCLA"), version=version.version,
                 distance=Decimal('11253'),
                 line_ref=getRef(line_ls),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SCLA-S"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s), onward_route_link_ref=getRef(rl_sl, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SCLA-L"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l)),
                   ])
                   )

route_shsa = Route(id=getId(Route, codespace, "SHSA"), version=version.version,
                 distance=Decimal('12179'),
                 line_ref=getRef(line_shsa),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SHSA-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h), onward_route_link_ref=getRef(rl_ha, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SHSA-A"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a)),
                   ])
                   )

route_sash = Route(id=getId(Route, codespace, "SASH"), version=version.version,
                 distance=Decimal('12179'),
                 line_ref=getRef(line_shsa),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SASH-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_a), onward_route_link_ref=getRef(rl_ah, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SASH-A"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_h)),
                   ])
                   )

route_slss = Route(id=getId(Route, codespace, "SLSS"), version=version.version,
                 distance=Decimal('11253'),
                 line_ref=getRef(line_slss),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SLSS-L"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l), onward_route_link_ref=getRef(rl_ls, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SLSS-S"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s)),
                   ])
                   )

route_sssl = Route(id=getId(Route, codespace, "SSSL"), version=version.version,
                 distance=Decimal('11253'),
                 line_ref=getRef(line_slss),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SSSL-S"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_s), onward_route_link_ref=getRef(rl_sl, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "SSSL-L"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_l)),
                   ])
                   )

routes = [route_hoam, route_amho, route_lasc, route_scla, route_sash, route_shsa, route_slss, route_sssl]



sa_h = StopArea(id=getId(StopArea, codespace, "HO"),
                 version=version.version,
                 name=MultilingualString(value="Holwerd"),
                 private_codes=PrivateCodes(private_code=[PrivateCode(value="1", type_value="UserStopAreaCode")]),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Harlingen"))
                 )

sa_a = StopArea(id=getId(StopArea, codespace, "AM"),
                 version=version.version,
                 name=MultilingualString(value="Ameland"),
                 private_codes=PrivateCodes(private_code=[PrivateCode(value="2", type_value="UserStopAreaCode")]),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Terschelling"))
                 )

sa_l = StopArea(id=getId(StopArea, codespace, "LA"),
                 version=version.version,
                 name=MultilingualString(value="Laurensoog"),
                 private_codes=PrivateCodes(private_code=[PrivateCode(value="3", type_value="UserStopAreaCode")]),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Vlieland"))
                 )

sa_s = StopArea(id=getId(StopArea, codespace, "SC"),
                 version=version.version,
                 name=MultilingualString(value="Schiermonnikoog"),
                 private_codes=PrivateCodes(private_code=[PrivateCode(value="4", type_value="UserStopAreaCode")]),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Vlieland"))
                 )

stop_areas=[sa_h, sa_a, sa_l, sa_s]

ssps['H'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_h)])
ssps['H'].private_codes=PrivateCodes(private_code=[PrivateCode(value="20650001", type_value="UserStopCode")])
ssps['A'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_a)])
ssps['A'].private_codes=PrivateCodes(private_code=[PrivateCode(value="29190001", type_value="UserStopCode")])
ssps['L'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_l)])
ssps['L'].private_codes=PrivateCodes(private_code=[PrivateCode(value="10380001", type_value="UserStopCode")])
ssps['S'].stop_areas = StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_s)])
ssps['S'].private_codes=PrivateCodes(private_code=[PrivateCode(value="29310001", type_value="UserStopCode")])

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
sjs: List[DatedServiceJourney] = [x for x in general_frame.members.choice if isinstance(x, DatedServiceJourney)]
sjps = {}
sjps_hash = {}
tls = {}
tdts = {}
tdts_hash = {}

tdtp = TimeDemandTypesProfile(codespace=codespace, version=version)

for sj in sjs:
    tdtp.getServiceJourneyPattern(sj, sjps, sjps_hash, ssps, tls)
    tdtp.getTimeDemandType(sj, sjps, tdts, tdts_hash, ssps, tls, None)
    """
    sj.private_code = PrivateCode(type_value="JourneyNumber", value=str(int(str(sj.departure_time).replace(':', ''))))
    if sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:AMHO', 'NL:WPD:ServiceJourneyPattern:HOAM'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_vieroerd, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:LASC', 'NL:WPD:ServiceJourneyPattern:SCLA'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_rottummonnik, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:SASH', 'NL:WPD:ServiceJourneyPattern:SHSA'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_fostaborg, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:SLSS', 'NL:WPD:ServiceJourneyPattern:SSSL'):
        sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type_esonborg, VehicleTypeRef)
    """

for tl in tls.values():
    tl: TimingLink
    f = tl.from_point_ref.ref.split(':')[-1]
    t = tl.to_point_ref.ref.split(':')[-1]
    for rl in route_links:
        if rl.from_point_ref.ref.endswith(':' + f) and rl.to_point_ref.ref.endswith(':' + t):
            tl.distance = rl.distance
            tl.operational_context_ref = rl.operational_context_ref

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id.replace(':DestinationDisplay:', ':DestinationDisplayVariant:') + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_ho = DestinationDisplay(id=getId(DestinationDisplay, codespace, "HO"), version=version.version,
                           name=MultilingualString(value="Holwerd"),
                           front_text=MultilingualString(value="Holwerd"),
                           private_codes=PrivateCodes(private_code=[PrivateCode(value="1", type_value="DestinationCode")]))
setVariants(dd_ho)

dd_am = DestinationDisplay(id=getId(DestinationDisplay, codespace, "AM"), version=version.version,
                           name=MultilingualString(value="Ameland"),
                           front_text=MultilingualString(value="Ameland"),
                           private_codes=PrivateCodes(private_code=[PrivateCode(value="2", type_value="DestinationCode")]))
setVariants(dd_am)

dd_la = DestinationDisplay(id=getId(DestinationDisplay, codespace, "LA"), version=version.version,
                           name=MultilingualString(value="Laurersoog"),
                           front_text=MultilingualString(value="Laurersoog"),
                           private_codes=PrivateCodes(private_code=[PrivateCode(value="3", type_value="DestinationCode")]))
setVariants(dd_la)

dd_sc = DestinationDisplay(id=getId(DestinationDisplay, codespace, "SC"), version=version.version,
                           name=MultilingualString(value="Schiermonnikoog"),
                           front_text=MultilingualString(value="Schiermonnikoog"),
                           private_codes=PrivateCodes(private_code=[PrivateCode(value="4", type_value="DestinationCode")]))
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
        version.start_date = ac.from_date
    if version.end_date.to_datetime() < ac.to_date.to_datetime():
        version.end_date = ac.to_date

notice_ovchipkaart = Notice(id=getId(Notice, codespace, "GeenOVchipkaart"), version=version.version,
                            can_be_advertised=True,
                            text=MultilingualString(value="Voor dit deel van de reis is betalen met de OV-chipkaart of OVpay niet mogelijk."))

notice_assignments = [NoticeAssignment(id=getId(NoticeAssignment, codespace, "GeenOVchipkaart-" + line.id.split(':')[-1]), version=version.version, order=1,
                     noticed_object_ref=getRef(line, VersionOfObjectRefStructure),
                     notice_ref_or_group_of_notices_ref_or_notice=getRef(notice_ovchipkaart)) for line in lines]


service_frames = dutchprofile.getServiceFrames(route_points=list(route_points.values()), route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=list(ssps.values()), stop_areas=stop_areas,
                                              stop_assignments=stop_assignments, timing_points=None, timing_links=list(tls.values()),
                                               service_journey_patterns=list(sjps.values()), time_demand_types=list(tdts.values()),
                                              notices=[notice_ovchipkaart], notice_assignments=notice_assignments)

sjp_idx = ['NL:WPD:ServiceJourneyPattern:AMHO', 'NL:WPD:ServiceJourneyPattern:HOAM',
 'NL:WPD:ServiceJourneyPattern:LASC', 'NL:WPD:ServiceJourneyPattern:SCLA',
 'NL:WPD:ServiceJourneyPattern:SASH', 'NL:WPD:ServiceJourneyPattern:SHSA',
 'NL:WPD:ServiceJourneyPattern:SLSS', 'NL:WPD:ServiceJourneyPattern:SSSL']

for sj in service_journeys:
    sjp_no = sjp_idx.index(sj.journey_pattern_ref.ref) + 1
    private_code = "{:d}{}".format(sjp_no, "{:04d}".format(int(str(sj.departure_time).replace(':', '')[0:4])))

    sj.private_codes = PrivateCodes(private_code=[PrivateCode(type_value="JourneyNumber", value=private_code)])
    if sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:AMHO', 'NL:WPD:ServiceJourneyPattern:HOAM'):
        sj.vehicle_type_ref_or_train_ref = getRef(vehicle_type_vieroerd, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:LASC', 'NL:WPD:ServiceJourneyPattern:SCLA'):
        sj.vehicle_type_ref_or_train_ref = getRef(vehicle_type_rottummonnik, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:SASH', 'NL:WPD:ServiceJourneyPattern:SHSA'):
        sj.vehicle_type_ref_or_train_ref = getRef(vehicle_type_fostaborg, VehicleTypeRef)
    elif sj.journey_pattern_ref.ref in ('NL:WPD:ServiceJourneyPattern:SLSS', 'NL:WPD:ServiceJourneyPattern:SSSL'):
        sj.vehicle_type_ref_or_train_ref = getRef(vehicle_type_esonborg, VehicleTypeRef)

timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions, operator_view=OperatorView(operator_ref=getRef(operator)), vehicle_journeys=service_journeys)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[dova_codespace, codespace], versions=[version], valid_between=valid_between,
                                                 responsibility_set=responsibility_set_partitie,
                                                 resource_frames=resource_frames, service_frames=service_frames, timetable_frames=timetable_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste WPD export")

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

"""
with open('netex-output/wpd.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)

parser = lxml.etree.XMLParser(remove_blank_text=True)
tree = lxml.etree.parse("netex-output/wpd.xml", parser=parser)
for element in tree.iterfind(".//*"):
    if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
        element.getparent().remove(element)
tree.write("netex-output/wpd-filter.xml", pretty_print=True, strip_text=True)
"""

from_date = datetime.date.today().isoformat().replace('-', '')

from isal import igzip_threaded
ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
with igzip_threaded.open(f"/tmp/NeTEx_WPD_WPD_{from_date}_{from_date}.xml.gz", 'wt', compresslevel=3, threads=3, block_size=2*10**8) as out:
    serializer.write(out, publication_delivery, ns_map)
