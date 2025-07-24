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
    NoticeAssignment, LineRefStructure

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
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 3, 11, 00, 00), datetime.datetime(2025, 7, 4, 11, 59, 00), datetime.timedelta(minutes=30))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 3,12, 00, 00), datetime.datetime(2025, 7, 3, 23, 59, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 4, 8, 00, 00), datetime.datetime(2025, 7, 4, 11, 59, 00), datetime.timedelta(minutes=30))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 4, 12, 00, 00), datetime.datetime(2025, 7, 5, 00, 30, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 5, 8, 00, 00), datetime.datetime(2025, 7, 5, 11, 59, 00), datetime.timedelta(minutes=30))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 5, 12, 00, 00), datetime.datetime(2025, 7, 6, 00, 30, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 6, 8, 00, 00), datetime.datetime(2025, 7, 6, 11, 59, 00), datetime.timedelta(minutes=30))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 6, 12, 00, 00), datetime.datetime(2025, 7, 7, 00, 30, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 7, 8, 00, 00), datetime.datetime(2025, 7, 7, 11, 59, 00), datetime.timedelta(minutes=30))
stt.simple_timetable_interval(simple_timetable, "NS", "DTRH", datetime.datetime(2025, 7, 7, 12, 00, 00), datetime.datetime(2025, 7, 7, 14, 00, 00), datetime.timedelta(minutes=10))

stt.simple_timetable_interval(simple_timetable, "DTRH", "NS", datetime.datetime(2025, 7, 3, 12, 30, 00), datetime.datetime(2025, 7, 4, 1, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DTRH", "NS", datetime.datetime(2025, 7, 4, 8, 0, 00), datetime.datetime(2025, 7, 5, 2, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DTRH", "NS", datetime.datetime(2025, 7, 5, 8, 30, 00), datetime.datetime(2025, 7, 6, 2, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DTRH", "NS", datetime.datetime(2025, 7, 6, 8, 30, 00), datetime.datetime(2025, 7, 7, 2, 00, 00), datetime.timedelta(minutes=10))
stt.simple_timetable_interval(simple_timetable, "DTRH", "NS", datetime.datetime(2025, 7, 7, 8, 00, 00), datetime.datetime(2025, 7, 7, 14, 00, 00), datetime.timedelta(minutes=10))


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

transport_administrative_zone_partitie = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "DTRH"),
                                                            version="any",
                                                            name=MultilingualString(value="MOJO Nijmegen"),
                                                            short_name=MultilingualString(value="MOJO-DTRH"),
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

line = Line(id=getId(Line, codespace, "MOJO-DTRH"), version=version.version, name=MultilingualString(value="MOJO"),
              monitored=False,
              external_line_ref=ExternalObjectRefStructure(type_value="VeTagLineNumber", ref="2"),
              responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Down The Rabbit Hole Pendelbus"),
              transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
              type_of_service_ref=TypeOfServiceRef(ref="NL:BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="MOJO"),
              private_codes=PrivateCodes(private_code=[PrivateCode(value="2", type_value="LinePlanningNumber")]),
              operator_ref=getRef(operator),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "MOJO"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.UNKNOWN)
              )

import json
import itertools
geojson = json.load(open("dtrh.geojson", 'r'))
# linestring_dtrhns = ' '.join([' '.join([str(y) for y in x]) for x in geojson['features'][0]['geometry']['coordinates']])
# linestring_nsdtrh = ' '.join([' '.join([str(y) for y in x]) for x in geojson['features'][1]['geometry']['coordinates']])

linestring_dtrhns = list(itertools.chain(*geojson['features'][0]['geometry']['coordinates']))
linestring_nsdtrh = list(itertools.chain(*geojson['features'][1]['geometry']['coordinates']))


rp_ns = RoutePoint(id=getId(RoutePoint, codespace, "NS"), version=version.version, location=LocationStructure2(pos=Pos(value=linestring_nsdtrh[0:2], srs_dimension=2)))
rp_dtrh = RoutePoint(id=getId(RoutePoint, codespace, "DTRH"), version=version.version, location=LocationStructure2(pos=Pos(value=linestring_dtrhns[0:2], srs_dimension=2)))


route_points = [rp_ns, rp_dtrh]

# linestring_nsdtrh = rp_ns.location.pos.value + rp_dtrh.location.pos.value # TODO

rl_nsdtrh = RouteLink(id=getId(RouteLink, codespace, "NS-DTRH"), version=version.version,
                  distance=Decimal('13340'), # TODO
                  from_point_ref=getRef(rp_ns, RoutePointRefStructure), to_point_ref=getRef(rp_dtrh, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "NS-DTRH").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=len(linestring_nsdtrh) // 2, value=linestring_nsdtrh)]),
                    operational_context_ref=getRef(operational_context))


# linestring_dtrhns = rp_dtrh.location.pos.value + rp_ns.location.pos.value # TODO

rl_dtrhns = RouteLink(id=getId(RouteLink, codespace, "DTRH-NS"), version=version.version,
                  distance=Decimal('14716'), # TODO
                  from_point_ref=getRef(rp_dtrh, RoutePointRefStructure), to_point_ref=getRef(rp_ns, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "DTRH-NS").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=len(linestring_dtrhns) // 2, value=linestring_dtrhns)]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_nsdtrh, rl_dtrhns]


route_nsdhrh = Route(id=getId(Route, codespace, "NS-DTRH"), version=version.version,
                 distance=Decimal('13340'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "NS-DTRH-NS"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_ns), onward_route_link_ref=getRef(rl_nsdtrh, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "NS-DTRH-DTRH"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_dtrh)),
                   ])
                   )

route_dtrhns = Route(id=getId(Route, codespace, "DTRH-NS"), version=version.version,
                 distance=Decimal('14716'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "DTRH-NS-DTRH"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_dtrh), onward_route_link_ref=getRef(rl_dtrhns, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "DTRH-NS-NS"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_ns)),
                   ])
                   )


routes = [route_nsdhrh, route_dtrhns]

lines = [line]

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id.replace(':DestinationDisplay:', ':DestinationDisplayVariant:') + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="NL:BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_ns = DestinationDisplay(id=getId(DestinationDisplay, codespace, "NS"), version=version.version,
                           name=MultilingualString(value="Nijmegen Station"),
                           front_text=MultilingualString(value="Nijmegen Station"),
                           private_codes=PrivateCodes(private_code=[PrivateCode(value="21", type_value="DestinationCode")]))
setVariants(dd_ns)

dd_dtrh = DestinationDisplay(id=getId(DestinationDisplay, codespace, "DTRH"), version=version.version,
                           name=MultilingualString(value="Down The Rabbit Hole"),
                           front_text=MultilingualString(value="Down The Rabbit Hole"),
                           private_codes=PrivateCodes(private_code=[PrivateCode(value="22", type_value="DestinationCode")]))
setVariants(dd_dtrh)

dd_dtrh.variants.destination_display_variant[2].name.value = 'DTRH'
dd_dtrh.variants.destination_display_variant[3].name.value = 'DTRH'


destination_displays=[dd_ns, dd_dtrh]

sa_ns = StopArea(id=getId(StopArea, codespace, "NS"),
                 version=version.version,
                 name=MultilingualString(value="Nijmegen Station"),
                 private_codes=PrivateCodes(private_code=PrivateCode(value="60007070", type_value="UserStopAreaCode")),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Nijmegen"))
                 )

sa_dtrh = StopArea(id=getId(StopArea, codespace, "DTRH"),
                 version=version.version,
                 name=MultilingualString(value="Dronten, Station"),
                 private_codes=PrivateCodes(private_code=PrivateCode(value="61220001", type_value="UserStopAreaCode")),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Ewijk"))
                 )

stop_areas=[sa_ns, sa_dtrh]

ssp_ns = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "NS"), version=version.version,
                              name=MultilingualString(value="Nijmegen CS"),
                              location=LocationStructure2(pos=Pos(value=[187128, 428503], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "NS"), version=version.version, project_to_point_ref=getRef(rp_ns, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_ns)]),
                              private_codes=PrivateCodes(private_code=PrivateCode(value="60007070", type_value="UserStopCode")))

ssp_dtrh = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "DTRH"), version=version.version,
                              name=MultilingualString(value="Ewijk, Ficarystraat"),
                              location=LocationStructure2(pos=Pos(value=[175844, 429459], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "DTRH"), version=version.version, project_to_point_ref=getRef(rp_dtrh, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_dtrh)]),
                              private_codes=PrivateCodes(private_code=PrivateCode(value="61220001", type_value="UserStopCode")))


scheduled_stop_points=[ssp_ns, ssp_dtrh]

tl_nsdhrh = TimingLink(id=getId(TimingLink, codespace, "NS-DTRH"), version=version.version,
                   distance=Decimal('13340'), # TODO
                   from_point_ref=getRef(ssp_ns, TimingPointRefStructure), to_point_ref=getRef(ssp_dtrh, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_dhrhns = TimingLink(id=getId(TimingLink, codespace, "DTRH-NS"), version=version.version,
                   distance=Decimal('14716'), # TODO
                   from_point_ref=getRef(ssp_dtrh, TimingPointRefStructure), to_point_ref=getRef(ssp_ns, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))


timing_links = [tl_nsdhrh, tl_dhrhns]

stop_assignments=[PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "NS"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_ns),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:60007070", QuayRef, "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "DTRH"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_dtrh),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:61220001", QuayRef, "any"))
                  ]

sjp_nsdhrh = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "NS-DTRH"), version=version.version,
                                 route_ref_or_route_view=getRef(route_nsdhrh),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_dtrh),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "NS-DTRH-NS"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_ns),
                                                                   onward_timing_link_ref=getRef(tl_nsdhrh, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "NS-DTRH-DTRH"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_dtrh)),
                                     ]
                                    )
                                 )

sjp_dhrhns = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "DTRH-NS"), version=version.version,
                                 route_ref_or_route_view=getRef(route_dtrhns),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_ns),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "DTRH-NS-DTRH"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_dtrh),
                                                                   onward_timing_link_ref=getRef(tl_dhrhns, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "DTRH-NS-NS"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_ns)),
                                     ]
                                    )
                                 )


journey_patterns=[sjp_dhrhns, sjp_nsdhrh]

tdt_nsdhrh = TimeDemandType(id=getId(TimeDemandType, codespace, "NS-DTRH"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "NS-DTRH"), version=version.version, timing_link_ref=getRef(tl_nsdhrh), run_time=XmlDuration("PT1440S"))]))

tdt_dhrhns = TimeDemandType(id=getId(TimeDemandType, codespace, "DTRH-NS"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "DTRH-NS"), version=version.version, timing_link_ref=getRef(tl_dhrhns), run_time=XmlDuration("PT1440S"))]))


time_demand_types=[tdt_nsdhrh, tdt_dhrhns]

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
with igzip_threaded.open(f"/tmp/NeTEx_MOJO_DTRH_{from_date}_{from_date}.xml.gz", 'wt', compresslevel=3, threads=3, block_size=2*10**8) as out:
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