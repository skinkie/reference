from _decimal import Decimal

import datetime
import gzip

from xsdata.formats.dataclass.models.generics import AnyElement
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime, XmlDuration

from dutchprofile import DutchProfile
from netex import Codespace, Version, VersionTypeEnumeration, DataSource, MultilingualString, ResponsibilitySet, \
    ResponsibilityRoleAssignmentsRelStructure, ResponsibilityRoleAssignment, VersionOfObjectRefStructure, Operator, \
    AllModesEnumeration, OrganisationTypeEnumeration, OperatorActivitiesEnumeration, OperationalContext, \
    AllVehicleModesOfTransportEnumeration, VehicleType, FuelTypeEnumeration, \
    FareClassEnumeration, ServiceFacilitySetsRelStructure, ServiceFacilitySet, MobilityFacilityEnumeration, \
    SanitaryFacilityEnumeration, VehicleAccessFacilityEnumeration, \
    TransportAdministrativeZone, RoutePoint, RouteLink, Route, \
    Line, DestinationDisplay, ScheduledStopPoint, StopArea, PassengerStopAssignment, TimingLink, ServiceJourneyPattern, \
    TimeDemandType, TypeOfServiceRef, AccessibilityAssessment, LimitationStatusEnumeration, LocationStructure2, Pos, \
    DirectionTypeEnumeration, PointsOnRouteRelStructure, PointOnRoute, PrivateCode, \
    DestinationDisplayVariantsRelStructure, DestinationDisplayVariant, Extensions2, DeliveryVariantTypeEnumeration, \
    ProjectionsRelStructure, PointProjection, StopAreaRefsRelStructure, TopographicPlaceView, \
    PointsInJourneyPatternRelStructure, StopPointInJourneyPattern, JourneyRunTimesRelStructure, JourneyRunTime, \
    TimingLinkRefStructure, PointRefStructure, RoutePointRefStructure, TimingPointRefStructure, LineString, PosList, \
    PassengerCapacitiesRelStructure, PassengerCapacity, RouteLinkRefStructure, OperatorView, QuayRef, \
    ContactStructure, Authority, TypeOfResponsibilityRoleRef, OrganisationRefStructure, ServiceJourney, \
    MobilityFacilityList, SanitaryFacilityList, \
    TicketingServiceFacilityList, TicketingServiceFacilityEnumeration, VehicleAccessFacilityList, DirectionType, \
    TransportTypeVersionStructure, PublicCodeStructure, ExternalObjectRefStructure, PrivateCodes, ValidBetween, Notice, \
    NoticeAssignment

from refs import getId, getRef, getFakeRef
from simpletimetable import SimpleTimetable

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

codespace_xmlns = "NL:MOJO"
short_name = "MOJO"

codespace = Codespace(id="NL:{}:Codespace:{}".format("BISON", short_name), xmlns=codespace_xmlns,
                      xmlns_url="http://bison.dova.nu/ns/MOJO", description=MultilingualString(value="MOJO"))

dova_codespace = Codespace(id="NL:{}:Codespace:{}".format("BISON", "DOVA"), xmlns="NL:DOVA",
                      xmlns_url="http://bison.dova.nu/ns/DOVA", description=MultilingualString(value="'Centrale' lijsten bijgehouden door DOVA"))

start_date = datetime.datetime(year=2024, month=8, day=15)
end_date = datetime.datetime(year=2024, month=8, day=19)

today = str(datetime.date.today()).replace('-', '')

version = Version(id=getId(Version, codespace, today),
                  version=today,
                  start_date=XmlDateTime.from_datetime(start_date),
                  end_date=XmlDateTime.from_datetime(end_date),
                  version_type=VersionTypeEnumeration.BASELINE)

valid_between = ValidBetween(from_date=XmlDateTime.from_datetime(start_date),
                             to_date=XmlDateTime.from_datetime(end_date))


stt = SimpleTimetable(codespace, version)
from_date = datetime.date.today().isoformat().replace('-', '')

simple_timetable = {}
stt.simple_timetable_interval(simple_timetable, "LY", "LO", datetime.datetime(2025, 8, 14, 7, 00, 00), datetime.datetime(2025, 8, 15, 00, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LY", "LO", datetime.datetime(2025, 8, 15, 8, 00, 00), datetime.datetime(2025, 8, 15, 17, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LY", "LO", datetime.datetime(2025, 8, 17, 17, 00, 00), datetime.datetime(2025, 8, 18, 00, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LY", "LO", datetime.datetime(2025, 8, 18, 8, 00, 00), datetime.datetime(2025, 8, 18, 13, 30, 00), datetime.timedelta(minutes=10))

stt.simple_timetable_interval(simple_timetable, "LO", "LY", datetime.datetime(2025, 8, 14, 7, 30, 00), datetime.datetime(2024, 8, 14, 23, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "LY", datetime.datetime(2025, 8, 15, 8, 00, 00), datetime.datetime(2024, 8, 15, 17, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "LY", datetime.datetime(2025, 8, 17, 16, 30, 00), datetime.datetime(2024, 8, 17, 23, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "LY", datetime.datetime(2025, 8, 18, 8, 00, 00), datetime.datetime(2024, 8, 18, 14, 00, 00), datetime.timedelta(minutes=10))

stt.simple_timetable_interval(simple_timetable, "DR", "LO", datetime.datetime(2025, 8, 14, 7, 00, 00), datetime.datetime(2025, 8, 16, 00, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DR", "LO", datetime.datetime(2025, 8, 16, 8, 00, 00), datetime.datetime(2025, 8, 17, 00, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DR", "LO", datetime.datetime(2025, 8, 17, 8, 00, 00), datetime.datetime(2025, 8, 18, 00, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DR", "LO", datetime.datetime(2025, 8, 18, 8, 00, 00), datetime.datetime(2025, 8, 19, 00, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DR", "LO", datetime.datetime(2025, 8, 19, 8, 00, 00), datetime.datetime(2025, 8, 19, 13, 30, 00), datetime.timedelta(minutes=10))

stt.simple_timetable_interval(simple_timetable, "LO", "DR", datetime.datetime(2025, 8, 14, 7, 30, 00), datetime.datetime(2025, 8, 14, 23, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "DR", datetime.datetime(2025, 8, 15, 8, 00, 00), datetime.datetime(2025, 8, 15, 23, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "DR", datetime.datetime(2025, 8, 16, 8, 00, 00), datetime.datetime(2025, 8, 16, 23, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "DR", datetime.datetime(2025, 8, 17, 8, 00, 00), datetime.datetime(2025, 8, 17, 23, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "LO", "DR", datetime.datetime(2025, 8, 18, 8, 00, 00), datetime.datetime(2025, 8, 18, 14, 00, 00), datetime.timedelta(minutes=10))


service_journeys, availability_conditions = stt.simple_timetable_from_dict(simple_timetable)

version.start_date = min([ac.from_date for ac in availability_conditions])
version.end_date = max([ac.to_date for ac in availability_conditions])

valid_between.from_date = min([ac.from_date for ac in availability_conditions])
valid_between.to_date = max([ac.to_date for ac in availability_conditions])


data_source = DataSource(id=getId(DataSource, codespace, short_name),
                         version=version.version,
                         name=MultilingualString(value=short_name),
                         short_name=MultilingualString(value=short_name),
                         description=MultilingualString(value=short_name))

transport_administrative_zone_partitie = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "Dronten"),
                                                            version="any",
                                                            name=MultilingualString(value="MOJO Dronten"),
                                                            short_name=MultilingualString(value="MOJOD"),
                                                            vehicle_modes=[AllModesEnumeration.BUS])


operator = Operator(id=getId(Operator, codespace, "MOJO"), version=version.version,
                        company_number="27223030",
                        name=MultilingualString(value="MOJO"),
                        short_name=MultilingualString(value="MOJO"),
                        legal_name=MultilingualString(value="MOJO Concerts B.V."),
                        organisation_type=[OrganisationTypeEnumeration.OPERATOR],
                        primary_mode=AllModesEnumeration.BUS,
                        contact_details=ContactStructure(url="https://mojo.nl/"),
                        customer_service_contact_details=ContactStructure(url="https://mojo.nl/"),
                        operator_activities=[OperatorActivitiesEnumeration.PASSENGER])

responsibility_set_financier = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, "Financier"),
                                       version=version.version,
                                       name=MultilingualString(value="Financier"),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(
                                               id=getId(ResponsibilityRoleAssignment, codespace, "Financier"),
                                               version=version.version,
                                               type_of_responsibility_role_ref_or_responsibility_role_ref=TypeOfResponsibilityRoleRef(ref="NL:BISON:TypeOfResponsibilityRole:financing", version="any"),
                                               responsible_organisation_ref=getRef(operator, OrganisationRefStructure)),
                                       ]))

responsibility_set_partitie = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, short_name),
                                       version=version.version,
                                       name=MultilingualString(value="Partitie"),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "Partitie"),
                                                                        version=version.version,
                                                                        responsible_area_ref=getRef(transport_administrative_zone_partitie, VersionOfObjectRefStructure))
                                       ]))

operational_context = OperationalContext(id=getId(OperationalContext, codespace, "BUS"), version=version.version,
                                       name=MultilingualString(value="BUS"), short_name=MultilingualString(value="BUS"),
                                         vehicle_mode=AllVehicleModesOfTransportEnumeration.BUS)

vehicle_type = VehicleType(id=getId(VehicleType, codespace, "Standaard"), version=version.version,
                           name=MultilingualString(value="Touringcar"),
                           description=MultilingualString(value="Touringcar"),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=[FuelTypeEnumeration.DIESEL]),
                           # fuel_type_or_type_of_fuel=TransportTypeVersionStructure.TypeOfFuel(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      [PassengerCapacity(id=getId(PassengerCapacity, codespace, "Standaard"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=80, seating_capacity=80)]),
                           transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                           length=Decimal("122"),
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               restricted_service_facility_set_ref_or_service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "Onbekend"), version=version.version,
                                                  mobility_facility_list=MobilityFacilityList(value=[MobilityFacilityEnumeration.UNKNOWN]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[VehicleAccessFacilityEnumeration.UNKNOWN]),
                                                  sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.NONE]),
                                                  )]
                           ))

sj: ServiceJourney
for sj in service_journeys:
    sj.vehicle_type_ref_or_train_ref = getRef(vehicle_type)

dutchprofile = DutchProfile(codespace, data_source, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set_financier, responsibility_set_partitie],
                                                 organisations=[operator], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type], zones=[transport_administrative_zone_partitie])

line = Line(id=getId(Line, codespace, "MOJO"), version=version.version, name=MultilingualString(value="MOJO"),
              monitored=False,
              external_line_ref=ExternalObjectRefStructure(type_value="VeTagLineNumber", ref="1"),
              responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Lowlands Pendelbus"),
              transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
              type_of_service_ref=TypeOfServiceRef(ref="NL:BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="MOJO"),
              private_codes=PrivateCodes(private_code=[PrivateCode(value="1", type_value="LinePlanningNumber")]),
              operator_ref=getRef(operator),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "MOJO"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.UNKNOWN)
              )


rp_ly = RoutePoint(id=getId(RoutePoint, codespace, "LY"), version=version.version, location=LocationStructure2(pos=Pos(value=[160611, 502254], srs_dimension=2)))
rp_dr = RoutePoint(id=getId(RoutePoint, codespace, "DR"), version=version.version, location=LocationStructure2(pos=Pos(value=[177667, 505203], srs_dimension=2)))
rp_lo = RoutePoint(id=getId(RoutePoint, codespace, "LO"), version=version.version, location=LocationStructure2(pos=Pos(value=[180461, 494075], srs_dimension=2)))


route_points = [rp_ly, rp_dr, rp_lo]

linestring_lylo = rp_ly.location.pos.value + rp_lo.location.pos.value # TODO

rl_lylo = RouteLink(id=getId(RouteLink, codespace, "LY-LO"), version=version.version,
                  distance=Decimal('30000'), # TODO
                  from_point_ref=getRef(rp_ly, RoutePointRefStructure), to_point_ref=getRef(rp_lo, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "LY-LO").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=len(linestring_lylo) // 2, value=linestring_lylo)]),
                    operational_context_ref=getRef(operational_context))


linestring_loly = rp_lo.location.pos.value + rp_ly.location.pos.value # TODO

rl_loly = RouteLink(id=getId(RouteLink, codespace, "LO-LY"), version=version.version,
                  distance=Decimal('30000'), # TODO
                  from_point_ref=getRef(rp_lo, RoutePointRefStructure), to_point_ref=getRef(rp_ly, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "LO-LY").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=len(linestring_loly) // 2, value=linestring_lylo)]),
                    operational_context_ref=getRef(operational_context))

linestring_drlo = rp_dr.location.pos.value + rp_lo.location.pos.value # TODO

rl_drlo = RouteLink(id=getId(RouteLink, codespace, "DR-LO"), version=version.version,
                  distance=Decimal('18000'), # TODO
                  from_point_ref=getRef(rp_dr, RoutePointRefStructure), to_point_ref=getRef(rp_lo, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "DR-LO").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=len(linestring_drlo) // 2, value=linestring_drlo)]),
                    operational_context_ref=getRef(operational_context))

linestring_lodr = rp_lo.location.pos.value + rp_dr.location.pos.value # TODO

rl_lodr = RouteLink(id=getId(RouteLink, codespace, "LO-DR"), version=version.version,
                  distance=Decimal('18000'), # TODO
                  from_point_ref=getRef(rp_lo, RoutePointRefStructure), to_point_ref=getRef(rp_dr, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "LO-DR").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=len(linestring_lodr) // 2, value=linestring_lodr)]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_lylo, rl_loly, rl_drlo, rl_lodr]



route_lylo = Route(id=getId(Route, codespace, "LY-LO"), version=version.version,
                 distance=Decimal('30000'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LY-LO-LY"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_ly), onward_route_link_ref=getRef(rl_lylo, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LY-LO-LO"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_lo)),
                   ])
                   )

route_loly = Route(id=getId(Route, codespace, "LO-LY"), version=version.version,
                 distance=Decimal('30000'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LO-LY-LO"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_lo), onward_route_link_ref=getRef(rl_loly, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LO-LY-LY"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_ly)),
                   ])
                   )

route_drlo = Route(id=getId(Route, codespace, "DR-LO"), version=version.version,
                 distance=Decimal('18000'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "DR-LO-DR"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_dr), onward_route_link_ref=getRef(rl_drlo, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "DR-LO-LO"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_lo)),
                   ])
                   )

route_lodr = Route(id=getId(Route, codespace, "LO-DR"), version=version.version,
                 distance=Decimal('18000'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LO-DR-DR"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_lo), onward_route_link_ref=getRef(rl_lodr, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "LO-DR-LO"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_dr)),
                   ])
                   )

routes = [route_lylo, route_loly, route_drlo, route_lodr]

lines = [line]

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id.replace(':DestinationDisplay:', ':DestinationDisplayVariant:') + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="NL:BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_ly = DestinationDisplay(id=getId(DestinationDisplay, codespace, "LY"), version=version.version,
                           name=MultilingualString(value="Station Lelystad"),
                           front_text=MultilingualString(value="Station Lelystad"),
                           private_codes=PrivateCodes(private_code=PrivateCode(value="1", type_value="DestinationCode")))
setVariants(dd_ly)

dd_dr = DestinationDisplay(id=getId(DestinationDisplay, codespace, "DR"), version=version.version,
                           name=MultilingualString(value="Station Dronten"),
                           front_text=MultilingualString(value="Station Dronten"),
                           private_codes=PrivateCodes(private_code=PrivateCode(value="2", type_value="DestinationCode")))
setVariants(dd_dr)

dd_lo = DestinationDisplay(id=getId(DestinationDisplay, codespace, "LO"), version=version.version,
                           name=MultilingualString(value="Lowlands"),
                           front_text=MultilingualString(value="Lowlands"),
                           private_codes=PrivateCodes(private_code=PrivateCode(value="3", type_value="DestinationCode")))
setVariants(dd_lo)


destination_displays=[dd_ly, dd_dr, dd_lo]

sa_ly = StopArea(id=getId(StopArea, codespace, "LY"),
                 version=version.version,
                 name=MultilingualString(value="Lelystad, Station Centrum"),
                 private_codes=PrivateCodes(private_code=PrivateCode(value="49000001", type_value="UserStopAreaCode")),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Lelystad"))
                 )


sa_dr = StopArea(id=getId(StopArea, codespace, "DR"),
                 version=version.version,
                 name=MultilingualString(value="Dronten, Station"),
                 private_codes=PrivateCodes(private_code=PrivateCode(value="49430390", type_value="UserStopAreaCode")),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Dronten"))
                 )

sa_lo = StopArea(id=getId(StopArea, codespace, "G"),
                 version=version.version,
                 name=MultilingualString(value="Biddinghuizen, Lowlands"),
                 private_codes=PrivateCodes(private_code=PrivateCode(value="49810001", type_value="UserStopAreaCode")),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Biddinghuizen"))
                 )

stop_areas=[sa_ly, sa_dr, sa_lo]

ssp_ly = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "LY"), version=version.version,
                              name=MultilingualString(value="Lelystad, Station Centrum"),
                              location=LocationStructure2(pos=Pos(value=[160611, 502254], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "LY"), version=version.version, project_to_point_ref=getRef(rp_ly, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_ly)]),
                              private_codes=PrivateCodes(private_code=PrivateCode(value="49000001", type_value="UserStopCode")))

ssp_dr = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "DR"), version=version.version,
                              name=MultilingualString(value="Dronten, Station"),
                              location=LocationStructure2(pos=Pos(value=[177667, 505203], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "DR"), version=version.version, project_to_point_ref=getRef(rp_dr, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_dr)]),
                              private_codes=PrivateCodes(private_code=PrivateCode(value="49430425", type_value="UserStopCode")))

ssp_lo = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "LO"), version=version.version,
                              name=MultilingualString(value="Biddinghuizen, Lowlands"),
                              location=LocationStructure2(pos=Pos(value=[180461, 494075], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "LO"), version=version.version, project_to_point_ref=getRef(rp_lo, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_lo)]),
                              private_codes=PrivateCodes(private_code=PrivateCode(value="49810001", type_value="UserStopCode")))


scheduled_stop_points=[ssp_ly, ssp_dr, ssp_lo]

tl_lylo = TimingLink(id=getId(TimingLink, codespace, "LY-LO"), version=version.version,
                   distance=Decimal('30000'), # TODO
                   from_point_ref=getRef(ssp_ly, TimingPointRefStructure), to_point_ref=getRef(ssp_lo, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_loly = TimingLink(id=getId(TimingLink, codespace, "LO-LY"), version=version.version,
                   distance=Decimal('30000'), # TODO
                   from_point_ref=getRef(ssp_lo, TimingPointRefStructure), to_point_ref=getRef(ssp_ly, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_drlo = TimingLink(id=getId(TimingLink, codespace, "DR-LO"), version=version.version,
                   distance=Decimal('18000'), # TODO
                   from_point_ref=getRef(ssp_dr, TimingPointRefStructure), to_point_ref=getRef(ssp_lo, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_lodr = TimingLink(id=getId(TimingLink, codespace, "LO-DR"), version=version.version,
                   distance=Decimal('18000'), # TODO
                   from_point_ref=getRef(ssp_lo, TimingPointRefStructure), to_point_ref=getRef(ssp_dr, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

timing_links = [tl_lylo, tl_loly, tl_drlo, tl_lodr]

stop_assignments=[PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "LY"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_ly),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:49000001", QuayRef, "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "LO"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_lo),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:49810001", QuayRef, "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "DR"), version=version.version,
                                          order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(
                                              ssp_dr),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:49430425", QuayRef,
                                                                                        "any")),
                  ]

sjp_lylo = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "LY-LO"), version=version.version,
                                 route_ref_or_route_view=getRef(route_lylo),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_lo),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "LY-LO-LY"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_ly),
                                                                   onward_timing_link_ref=getRef(tl_lylo, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "LY-LO-LO"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_lo)),
                                     ]
                                    )
                                 )

sjp_loly = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "LO-LY"), version=version.version,
                                 route_ref_or_route_view=getRef(route_loly),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_ly),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "LO-LY-LO"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_lo),
                                                                   onward_timing_link_ref=getRef(tl_loly, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "LO-LY-LY"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_ly)),
                                     ]
                                    )
                                 )

sjp_drlo = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "DR-LO"), version=version.version,
                                 route_ref_or_route_view=getRef(route_drlo),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_lo),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "DR-LO-DR"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_dr),
                                                                   onward_timing_link_ref=getRef(tl_drlo, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "DR-LO-LO"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_lo)),
                                     ]
                                    )
                                 )

sjp_lodr = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "LO-DR"), version=version.version,
                                 route_ref_or_route_view=getRef(route_lodr),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_dr),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "LO-DR-LO"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_lo),
                                                                   onward_timing_link_ref=getRef(tl_lodr, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "LO-DR-DR"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_dr)),
                                     ]
                                    )
                                 )


journey_patterns=[sjp_loly, sjp_lylo, sjp_drlo, sjp_lodr]

tdt_lylo = TimeDemandType(id=getId(TimeDemandType, codespace, "LY-LO"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "LY-LO"), version=version.version, timing_link_ref=getRef(tl_lylo), run_time=XmlDuration("PT1800S"))]))

tdt_loly = TimeDemandType(id=getId(TimeDemandType, codespace, "LO-LY"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "LO-LY"), version=version.version, timing_link_ref=getRef(tl_loly), run_time=XmlDuration("PT1800S"))]))

tdt_drlo = TimeDemandType(id=getId(TimeDemandType, codespace, "DR-LO"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "DR-LO"), version=version.version, timing_link_ref=getRef(tl_drlo), run_time=XmlDuration("PT1200S"))]))

tdt_lodr = TimeDemandType(id=getId(TimeDemandType, codespace, "LO-DR"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "LO-DR"), version=version.version, timing_link_ref=getRef(tl_lodr), run_time=XmlDuration("PT1200S"))]))

time_demand_types=[tdt_lylo, tdt_loly, tdt_drlo, tdt_lodr]

notice = Notice(id=getId(Notice, codespace, "MOJO"), version=version.version, text=MultilingualString(value="Deze ritten zijn gratis toegankelijk voor festivalbezoekers."))
notice_assignment = NoticeAssignment(id=getId(NoticeAssignment, codespace, "MOJO"), version=version.version, order=1, notice_ref_or_group_of_notices_ref_or_notice=getRef(notice), noticed_object_ref=getRef(line, VersionOfObjectRefStructure))

service_frames = dutchprofile.getServiceFrames(route_points=route_points, route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=scheduled_stop_points, stop_areas=stop_areas,
                                              stop_assignments=stop_assignments, timing_points=None, timing_links=timing_links, service_journey_patterns=journey_patterns, time_demand_types=time_demand_types,
                                              notices=[notice], notice_assignments=[notice_assignment])


timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions, operator_view=OperatorView(operator_ref=getRef(operator)), vehicle_journeys=service_journeys)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[codespace], versions=[version], valid_between=valid_between,
                                                 responsibility_set=responsibility_set_partitie,
                                                 resource_frames=resource_frames, service_frames=service_frames, timetable_frames=timetable_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="MOJO export")

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

from isal import igzip_threaded
import gzip
ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
with igzip_threaded.open(f"/tmp/NeTEx_MOJO_MOJO_{from_date}_{from_date}.xml.gz", 'wt', compresslevel=3, threads=3, block_size=2*10**8) as out:
    serializer.write(out, publication_delivery, ns_map)


# with open('netex-output/wsf.xml', 'w', encoding='utf-8') as out:
#    serializer.write(out, publication_delivery, ns_map)

# with open('netex-output/wsf.xml', 'rb') as f_in, gzip.open(f"/tmp/NeTEx_WSF_WSF_{from_date}_{from_date}.xml.gz", 'wb') as f_out:
#   f_out.writelines(f_in)

"""
parser = lxml.etree.XMLParser(remove_blank_text=True)
tree = lxml.etree.parse("netex-output/wsf.xml", parser=parser)
for element in tree.iterfind(".//*"):
    if element.text is None and len(element) == 0 and len(element.attrib.keys()) == 0:
        element.getparent().remove(element)
tree.write(f"/tmp/NeTEx_WSF_{from_date}_{from_date}.xml", pretty_print=True, strip_text=True)
"""