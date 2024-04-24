from _decimal import Decimal

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.parsers.handlers import lxml
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
    PassengerCapacitiesRelStructure, PassengerCapacity, RouteLinkRefStructure, OperatorView, Quay, QuayRef, \
    ContactStructure, Authority, TypeOfResponsibilityRoleRef, AuthorityRef, OrganisationRefStructure, ServiceJourney, \
    DirectionType
import datetime

from refs import getId, getRef, getFakeRef
from simpletimetable import SimpleTimetable

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

short_name = "DOEKSEN"

codespace = Codespace(id="{}:Codespace:{}".format("BISON", short_name), xmlns=short_name,
                      xmlns_url="http://bison.dova.nu/ns/DOEKSEN", description="Rederij Doeksen")

dova_codespace = Codespace(id="{}:Codespace:{}".format("BISON", "DOVA"), xmlns="DOVA",
                      xmlns_url="http://bison.dova.nu/ns/DOVA", description="'Centrale' lijsten bijgehouden door DOVA")

start_date = datetime.datetime(year=2023, month=11, day=29)
end_date = datetime.datetime(year=2023, month=12, day=29)

version = Version(id=getId(Version, codespace, str(1)),
                  version=str(1),
                  start_date=XmlDateTime.from_datetime(start_date),
                  end_date=XmlDateTime.from_datetime(end_date),
                  version_type=VersionTypeEnumeration.BASELINE)

stt = SimpleTimetable(codespace, version)
service_journeys, availability_conditions, time_demand_types = stt.simple_timetable2('../doeksen/scrape-output/doeksen-20231206.csv')

for ac in availability_conditions:
    if version.start_date.to_datetime() > ac.from_date.to_datetime():
        version.start_date = ac.from_date.to
    if version.end_date.to_datetime() < ac.to_date.to_datetime():
        version.end_date = ac.to_date


data_source = DataSource(id=getId(DataSource, codespace, short_name),
                         version=version.version,
                         name=MultilingualString(value=short_name),
                         short_name=MultilingualString(value=short_name),
                         description=MultilingualString(value=short_name))

transport_administrative_zone = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "DOEKSEN"),
                                                            version="any",
                                                            name=MultilingualString(value="Veerdienst Harlingen-Vlieland-Terschelling"),
                                                            short_name=MultilingualString(value="DOEKSEN"),
                                                            vehicle_modes=[AllModesEnumeration.FERRY])

operator = Operator(id=getId(Operator, codespace, "DOEKSEN"), version=version.version,
                        company_number="01002252",
                        name=MultilingualString(value="Rederij Doeksen"),
                        short_name=MultilingualString(value="Doeksen"),
                        legal_name=MultilingualString(value="B.V. Rederij G. Doeksen en Zonen"),
                        organisation_type=[OrganisationTypeEnumeration.OPERATOR],
                        primary_mode=AllModesEnumeration.FERRY,
                        contact_details=ContactStructure(url="https://www.rederij-doeksen.nl/"),
                        customer_service_contact_details=ContactStructure(email="info@rederij-doeksen.nl", phone="+31889000888", url="https://www.rederij-doeksen.nl/"),
                        operator_activities=[OperatorActivitiesEnumeration.PASSENGER])

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
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "DOEKSEN"),
                                                                        version=version.version,
                                                                        data_role_type=None,
                                                                        stakeholder_role_type=None,
                                                                        responsible_area_ref=getRef(transport_administrative_zone, VersionOfObjectRefStructure))
                                       ]))


operational_context = OperationalContext(id=getId(OperationalContext, codespace, "WATER"), version=version.version,
                                       name=MultilingualString(value="WATER"), short_name=MultilingualString(value="WATER"),
                                         vehicle_mode=AllVehicleModesOfTransportEnumeration.FERRY)

vehicle_type_wdv = VehicleType(id=getId(VehicleType, codespace, "WDV"), version=version.version,
                           name=MultilingualString(value="Willem de Vlamingh"),
                           description=MultilingualString(value="Willem de Vlamingh"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.NATURAL_GAS,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "WDV"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=692)),
                           length=Decimal(value='70'), width=Decimal(value='17.3'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "WDV"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

vehicle_type_wb = VehicleType(id=getId(VehicleType, codespace, "WB"), version=version.version,
                           name=MultilingualString(value="Willem Barentsz"),
                           description=MultilingualString(value="Willem Barentsz"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.NATURAL_GAS,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "WB"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=692)),
                           length=Decimal(value='70'), width=Decimal(value='17.3'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "WB"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))


vehicle_type_friesland = VehicleType(id=getId(VehicleType, codespace, "FR"), version=version.version,
                           name=MultilingualString(value="Friesland"),
                           description=MultilingualString(value="Friesland"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "FRIESLAND"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=1100)),
                           length=Decimal(value='69'), width=Decimal(value='16'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "FRIESLAND"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

vehicle_type_vlieland = VehicleType(id=getId(VehicleType, codespace, "VL"), version=version.version,
                           name=MultilingualString(value="Vlieland"),
                           description=MultilingualString(value="Vlieland"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "VL"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=950)),
                           length=Decimal(value='68'), width=Decimal(value='17'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "VL"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   passenger_comms_facility_list=[
                                                       PassengerCommsFacilityEnumeration.FREE_WIFI],
                                                   sanitary_facility_list=[SanitaryFacilityEnumeration.TOILET,
                                                                           SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET],
                                                   meal_facility_list=[MealFacilityEnumeration.LUNCH,
                                                                       MealFacilityEnumeration.BREAKFAST,
                                                                       MealFacilityEnumeration.SNACK,
                                                                       MealFacilityEnumeration.DRINKS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

vehicle_type_koegelwieck = VehicleType(id=getId(VehicleType, codespace, "KW"), version=version.version,
                           name=MultilingualString(value="Koegelwieck"),
                           description=MultilingualString(value="Koegelwieck"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "KW"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=312)),
                           length=Decimal(value='35.5'), width=Decimal(value='17'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "KW"), version=version.version,
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

vehicle_type_tiger = VehicleType(id=getId(VehicleType, codespace, "TI"), version=version.version,
                           name=MultilingualString(value="Tiger"),
                           description=MultilingualString(value="Tiger"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "TI"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=414)),
                           length=Decimal(value='52'), width=Decimal(value='12'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "TI"), version=version.version,
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

vehicle_type_zeehond = VehicleType(id=getId(VehicleType, codespace, "ZEE"), version=version.version,
                           name=MultilingualString(value="Zeehond"),
                           description=MultilingualString(value="Zeehond"),
                           fuel_type_or_type_of_fuel=FuelTypeEnumeration.DIESEL,
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      PassengerCapacity(id=getId(PassengerCapacity, codespace, "ZEE"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=12)),
                           length=Decimal(value='13'), width=Decimal(value='5'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "ZEE"), version=version.version,
                                                   mobility_facility_list=[
                                                       MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS],
                                                   assistance_facility_list=[
                                                       AssistanceFacilityEnumeration.BOARDING_ASSISTANCE],
                                                   vehicle_access_facility_list=[
                                                       VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]
                           )]))

dutchprofile = DutchProfile(codespace, data_source, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set],
                                                 organisations=[operator, authority], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type_tiger,
                                                                vehicle_type_koegelwieck,
                                                                vehicle_type_zeehond,
                                                                vehicle_type_vlieland,
                                                                vehicle_type_wdv,
                                                                vehicle_type_wb,
                                                                vehicle_type_friesland], zones=[transport_administrative_zone])

line_ht = Line(id=getId(Line, codespace, "HT"), version=version.version, name=MultilingualString(value="Harlingen - Terschelling"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Harlingen en Terschelling"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="HT",
              private_code=PrivateCode(value="1", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "HT"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_hv = Line(id=getId(Line, codespace, "HV"), version=version.version, name=MultilingualString(value="Harlingen - Vlieland"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Harlingen en Vlieland"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="HT",
              private_code=PrivateCode(value="2", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "HV"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

line_tv = Line(id=getId(Line, codespace, "TV"), version=version.version, name=MultilingualString(value="Terschelling - Vlieland"),
              monitored=False,
              responsibility_set_ref_attribute=getId(ResponsibilitySet, codespace, short_name),
              description=MultilingualString(value="Veer tussen Terschelling en Vlieland"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code="HT",
              private_code=PrivateCode(value="3", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "TV"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )

rp_th = RoutePoint(id=getId(RoutePoint, codespace, "TH"), version=version.version, location=LocationStructure2(pos=Pos(value=[143673, 596725], srs_dimension=2)))
rp_tv = RoutePoint(id=getId(RoutePoint, codespace, "TV"), version=version.version, location=LocationStructure2(pos=Pos(value=[143584, 596671], srs_dimension=2)))

rp_v = RoutePoint(id=getId(RoutePoint, codespace, "V"), version=version.version, location=LocationStructure2(pos=Pos(value=[134235, 589993], srs_dimension=2)))

rp_hv = RoutePoint(id=getId(RoutePoint, codespace, "HV"), version=version.version, location=LocationStructure2(pos=Pos(value=[156671, 576646], srs_dimension=2)))
rp_ht = RoutePoint(id=getId(RoutePoint, codespace, "HT"), version=version.version, location=LocationStructure2(pos=Pos(value=[156806, 576728], srs_dimension=2)))

route_points = [rp_th, rp_tv, rp_v, rp_hv, rp_ht]

rl_th = RouteLink(id=getId(RouteLink, codespace, "T-H"), version=version.version,
                  distance=Decimal('43000'),
                  from_point_ref=getRef(rp_th, RoutePointRefStructure), to_point_ref=getRef(rp_ht, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "T-H").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_th.location.pos.value + rp_ht.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_ht = RouteLink(id=getId(RouteLink, codespace, "H-T"), version=version.version,
                  distance=Decimal('43000'),
                  from_point_ref=getRef(rp_ht, RoutePointRefStructure), to_point_ref=getRef(rp_th, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "H-T").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_ht.location.pos.value + rp_th.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_hv = RouteLink(id=getId(RouteLink, codespace, "H-V"), version=version.version,
                  distance=Decimal('43000'),
                  from_point_ref=getRef(rp_hv, RoutePointRefStructure), to_point_ref=getRef(rp_v, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "H-V").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_hv.location.pos.value + rp_v.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_vh = RouteLink(id=getId(RouteLink, codespace, "V-H"), version=version.version,
                  distance=Decimal('43000'),
                  from_point_ref=getRef(rp_v, RoutePointRefStructure), to_point_ref=getRef(rp_hv, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "V-H").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_v.location.pos.value + rp_hv.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_vt = RouteLink(id=getId(RouteLink, codespace, "V-T"), version=version.version,
                  distance=Decimal('16000'),
                  from_point_ref=getRef(rp_v, RoutePointRefStructure), to_point_ref=getRef(rp_tv, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "V-T").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_v.location.pos.value + rp_tv.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_tv = RouteLink(id=getId(RouteLink, codespace, "T-V"), version=version.version,
                  distance=Decimal('16000'),
                  from_point_ref=getRef(rp_tv, RoutePointRefStructure), to_point_ref=getRef(rp_v, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "T-V").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_tv.location.pos.value + rp_v.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))




route_links = [rl_th, rl_ht, rl_hv, rl_vh, rl_vt, rl_tv]


route_th = Route(id=getId(Route, codespace, "T-H"), version=version.version,
                 distance=Decimal('43000'),
                 line_ref=getRef(line_ht),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "T-H-T"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_th), onward_route_link_ref=getRef(rl_th, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "T-H-H"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_ht)),
                   ])
                   )

route_ht = Route(id=getId(Route, codespace, "H-T"), version=version.version,
                 distance=Decimal('43000'),
                 line_ref=getRef(line_ht),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "H-T-H"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_ht), onward_route_link_ref=getRef(rl_ht, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "H-T-T"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_th)),
                   ])
                   )

route_vh = Route(id=getId(Route, codespace, "V-H"), version=version.version,
                 distance=Decimal('43000'),
                 line_ref=getRef(line_hv),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "V-H-T"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_v), onward_route_link_ref=getRef(rl_vh, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "V-H-H"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_hv)),
                   ])
                   )

route_hv = Route(id=getId(Route, codespace, "H-V"), version=version.version,
                 distance=Decimal('43000'),
                 line_ref=getRef(line_hv),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "H-V-T"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_hv), onward_route_link_ref=getRef(rl_hv, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "H-V-H"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_v)),
                   ])
                   )

route_tv = Route(id=getId(Route, codespace, "T-V"), version=version.version,
                 distance=Decimal('16000'),
                 line_ref=getRef(line_tv),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "T-V-T"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_tv), onward_route_link_ref=getRef(rl_tv, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "T-V-V"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_v)),
                   ])
                   )

route_vt = Route(id=getId(Route, codespace, "V-T"), version=version.version,
                 distance=Decimal('16000'),
                 line_ref=getRef(line_tv),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "V-T-V"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_v), onward_route_link_ref=getRef(rl_vt, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "V-T-T"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_tv)),
                   ])
                   )

routes = [route_th, route_ht, route_vh, route_hv, route_tv, route_vt]

lines = [line_hv, line_tv, line_ht]

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_h = DestinationDisplay(id=getId(DestinationDisplay, codespace, "H"), version=version.version,
                           name=MultilingualString(value="Harlingen"),
                           front_text=MultilingualString(value="Harlingen"),
                           private_code=PrivateCode(value="1", type_value="DestinationCode"))
setVariants(dd_h)

dd_t = DestinationDisplay(id=getId(DestinationDisplay, codespace, "T"), version=version.version,
                           name=MultilingualString(value="Terschelling"),
                           front_text=MultilingualString(value="Terschelling"),
                           private_code=PrivateCode(value="2", type_value="DestinationCode"))
setVariants(dd_t)

dd_v = DestinationDisplay(id=getId(DestinationDisplay, codespace, "V"), version=version.version,
                           name=MultilingualString(value="Vlieland"),
                           front_text=MultilingualString(value="Vlieland"),
                           private_code=PrivateCode(value="3", type_value="DestinationCode"))
setVariants(dd_v)


destination_displays=[dd_h, dd_t, dd_v]


sa_h = StopArea(id=getId(StopArea, codespace, "H"),
                 version=version.version,
                 name=MultilingualString(value="Harlingen"),
                 private_code=PrivateCode(value="1", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Harlingen"))
                 )

sa_t = StopArea(id=getId(StopArea, codespace, "T"),
                 version=version.version,
                 name=MultilingualString(value="Terschelling"),
                 private_code=PrivateCode(value="2", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Terschelling"))
                 )

sa_v = StopArea(id=getId(StopArea, codespace, "V"),
                 version=version.version,
                 name=MultilingualString(value="Vlieland"),
                 private_code=PrivateCode(value="3", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Vlieland"))
                 )

stop_areas=[sa_h, sa_t, sa_v]



ssp_ht = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "HT"), version=version.version,
                              name=MultilingualString(value="Harlingen"),
                              location=LocationStructure2(pos=Pos(value=[156806, 576728], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "HT"), version=version.version, project_to_point_ref=getRef(rp_ht, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_h)]),
                              private_code=PrivateCode(value="20670002", type_value="UserStopCode"))

ssp_hv = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "HV"), version=version.version,
                              name=MultilingualString(value="Harlingen"),
                              location=LocationStructure2(pos=Pos(value=[156671, 576646], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "HV"), version=version.version, project_to_point_ref=getRef(rp_hv, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_h)]),
                              private_code=PrivateCode(value="20670003", type_value="UserStopCode"))

ssp_th = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "TH"), version=version.version,
                              name=MultilingualString(value="Terschelling"),
                              location=LocationStructure2(pos=Pos(value=[143673, 596725], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "TH"), version=version.version, project_to_point_ref=getRef(rp_th, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_t)]),
                              private_code=PrivateCode(value="29110001", type_value="UserStopCode"))

ssp_tv = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "TV"), version=version.version,
                              name=MultilingualString(value="Terschelling"),
                              location=LocationStructure2(pos=Pos(value=[143584, 596671], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "TV"), version=version.version, project_to_point_ref=getRef(rp_tv, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_t)]),
                              private_code=PrivateCode(value="29110003", type_value="UserStopCode"))

ssp_v = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "V"), version=version.version,
                              name=MultilingualString(value="Vlieland"),
                              location=LocationStructure2(pos=Pos(value=[134235, 589993], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "V"), version=version.version, project_to_point_ref=getRef(rp_v, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_v)]),
                              private_code=PrivateCode(value="29010001", type_value="UserStopCode"))



scheduled_stop_points=[ssp_ht, ssp_hv, ssp_th, ssp_tv, ssp_v]



tl_ht = TimingLink(id=getId(TimingLink, codespace, "HT-TH"), version=version.version,
                   distance=Decimal('43000'),
                   from_point_ref=getRef(ssp_ht, TimingPointRefStructure), to_point_ref=getRef(ssp_th, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_th = TimingLink(id=getId(TimingLink, codespace, "TH-HT"), version=version.version,
                   distance=Decimal('43000'),
                   from_point_ref=getRef(ssp_th, TimingPointRefStructure), to_point_ref=getRef(ssp_ht, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_hv = TimingLink(id=getId(TimingLink, codespace, "HV-V"), version=version.version,
                   distance=Decimal('43000'),
                   from_point_ref=getRef(ssp_hv, TimingPointRefStructure), to_point_ref=getRef(ssp_v, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_vh = TimingLink(id=getId(TimingLink, codespace, "V-HV"), version=version.version,
                   distance=Decimal('43000'),
                   from_point_ref=getRef(ssp_v, TimingPointRefStructure), to_point_ref=getRef(ssp_hv, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_vt = TimingLink(id=getId(TimingLink, codespace, "V-TV"), version=version.version,
                   distance=Decimal('16000'),
                   from_point_ref=getRef(ssp_v, TimingPointRefStructure), to_point_ref=getRef(ssp_tv, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_tv = TimingLink(id=getId(TimingLink, codespace, "TV-V"), version=version.version,
                   distance=Decimal('16000'),
                   from_point_ref=getRef(ssp_tv, TimingPointRefStructure), to_point_ref=getRef(ssp_v, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))


timing_links = [tl_th, tl_ht, tl_vh, tl_hv, tl_tv, tl_vt]



stop_assignments=[PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "HT"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_v),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:20670002", QuayRef, "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "HV"), version=version.version,
                                          order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(
                                              ssp_v),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:20670003", QuayRef,
                                                                                        "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "TH"), version=version.version,
                                          order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(
                                              ssp_v),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:29110001", QuayRef,
                                                                                        "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "TV"), version=version.version,
                                          order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(
                                              ssp_v),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:29110003", QuayRef,
                                                                                        "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "V"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_v),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:29010001", QuayRef, "any"))]

sjp_ht = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "HT-TH"), version=version.version,
                                 route_ref_or_route_view=getRef(route_ht),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_t),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "H-T-H"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_ht),
                                                                   onward_timing_link_ref=getRef(tl_ht, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "H-T-T"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_th)),
                                     ]
                                    )
                                 )

sjp_th = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "TH-HT"), version=version.version,
                                 route_ref_or_route_view=getRef(route_th),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_h),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "T-H-T"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_th),
                                                                   onward_timing_link_ref=getRef(tl_th, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "T-H-H"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_ht)),
                                     ]
                                    )
                                 )

sjp_hv = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "HV-V"), version=version.version,
                                 route_ref_or_route_view=getRef(route_hv),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_v),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "H-V-H"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_hv),
                                                                   onward_timing_link_ref=getRef(tl_hv, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "H-V-V"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_v)),
                                     ]
                                    )
                                 )

sjp_vh = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "V-HV"), version=version.version,
                                 route_ref_or_route_view=getRef(route_vh),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_h),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "V-H-V"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_v),
                                                                   onward_timing_link_ref=getRef(tl_vh, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "V-H-H"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_hv)),
                                     ]
                                    )
                                 )

sjp_vt = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "V-TV"), version=version.version,
                                 route_ref_or_route_view=getRef(route_vt),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_t),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "V-T-H"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_v),
                                                                   onward_timing_link_ref=getRef(tl_vt, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "V-T-T"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_tv)),
                                     ]
                                    )
                                 )

sjp_tv = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "TV-V"), version=version.version,
                                 route_ref_or_route_view=getRef(route_tv),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_v),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "T-V-T"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_tv),
                                                                   onward_timing_link_ref=getRef(tl_tv, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "T-V-V"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_v)),
                                     ]
                                    )
                                 )


journey_patterns=[sjp_ht, sjp_th, sjp_hv, sjp_vh, sjp_vt, sjp_tv]

service_frames = dutchprofile.getServiceFrames(route_points=route_points, route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=scheduled_stop_points, stop_areas=stop_areas,
                                              stop_assignments=stop_assignments, timing_points=None, timing_links=timing_links, service_journey_patterns=journey_patterns, time_demand_types=time_demand_types,
                                              notices=None, notice_assignments=None)


timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions, operator_view=OperatorView(operator_ref=getRef(operator)), vehicle_journeys=service_journeys)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[codespace], versions=[version],
                                                 responsibility_set=responsibility_set,
                                                 resource_frames=resource_frames, service_frames=service_frames, timetable_frames=timetable_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste Doeksen export")

serializer_config = SerializerConfig(ignore_default_attributes=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

with open('netex-output/doeksen.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)

parser = lxml.etree.XMLParser(remove_blank_text=True)
tree = lxml.etree.parse("netex-output/doeksen.xml", parser=parser)
for element in tree.iterfind(".//*"):
    if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
        element.getparent().remove(element)
tree.write("netex-output/doeksen-filter.xml", pretty_print=True, strip_text=True)
