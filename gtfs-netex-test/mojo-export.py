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
    TransportTypeVersionStructure, PublicCodeStructure

from refs import getId, getRef, getFakeRef
from simpletimetable import SimpleTimetable

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

short_name = "OPENOV"

codespace = Codespace(id="{}:Codespace:{}".format("BISON", short_name), xmlns=short_name,
                      xmlns_url="http://bison.dova.nu/ns/OPENOV", description=MultilingualString(value="openOV"))

dova_codespace = Codespace(id="{}:Codespace:{}".format("BISON", "DOVA"), xmlns="DOVA",
                      xmlns_url="http://bison.dova.nu/ns/DOVA", description=MultilingualString(value="'Centrale' lijsten bijgehouden door DOVA"))

start_date = datetime.datetime(year=2024, month=6, day=18)
end_date = datetime.datetime(year=2024, month=6, day=19)

today = str(datetime.date.today()).replace('-', '')

version = Version(id=getId(Version, codespace, today),
                  version=today,
                  start_date=XmlDateTime.from_datetime(start_date),
                  end_date=XmlDateTime.from_datetime(end_date),
                  version_type=VersionTypeEnumeration.BASELINE)

stt = SimpleTimetable(codespace, version)
from_date = datetime.date.today().isoformat().replace('-', '')

simple_timetable = {}
stt.simple_timetable_interval(simple_timetable, "N", "G", datetime.datetime(2024, 6, 18, 13, 00, 00), datetime.datetime(2024, 6, 18, 21, 00, 00), datetime.timedelta(minutes=5))
stt.simple_timetable_interval(simple_timetable,"N", "G", datetime.datetime(2024, 6, 19, 13, 00, 00), datetime.datetime(2024, 6, 19, 21, 00, 00), datetime.timedelta(minutes=5))
stt.simple_timetable_interval(simple_timetable,"G", "N", datetime.datetime(2024, 6, 18, 13, 00, 00), datetime.datetime(2024, 6, 19, 1, 00, 00), datetime.timedelta(minutes=5))
stt.simple_timetable_interval(simple_timetable,"G", "N", datetime.datetime(2024, 6, 19, 13, 00, 00), datetime.datetime(2024, 6, 20, 1, 00, 00), datetime.timedelta(minutes=5))


service_journeys, availability_conditions = stt.simple_timetable_from_dict(simple_timetable)

version.start_date = availability_conditions[0].from_date
version.end_date = availability_conditions[0].to_date

data_source = DataSource(id=getId(DataSource, codespace, short_name),
                         version=version.version,
                         name=MultilingualString(value=short_name),
                         short_name=MultilingualString(value=short_name),
                         description=MultilingualString(value=short_name))

transport_administrative_zone_partitie = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "Nijmegen"),
                                                            version="any",
                                                            name=MultilingualString(value="MOJO Nijmegen"),
                                                            short_name=MultilingualString(value="MOJON"),
                                                            vehicle_modes=[AllModesEnumeration.WATER])


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
                                               type_of_responsibility_role_ref_or_responsibility_role_ref=TypeOfResponsibilityRoleRef(ref="BISON:TypeOfResponsibilityRole:financing", version="any"),
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
                           # fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=[FuelTypeEnumeration.DIESEL]),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.TypeOfFuel(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      [PassengerCapacity(id=getId(PassengerCapacity, codespace, "Standaard"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=80, seating_capacity=80)]),
                           transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "Onbekend"), version=version.version,
                                                  mobility_facility_list=MobilityFacilityList(value=[MobilityFacilityEnumeration.UNKNOWN]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[VehicleAccessFacilityEnumeration.UNKNOWN]),
                                                  sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.NONE]),
                                                  )]
                           ))

sj: ServiceJourney
for sj in service_journeys:
    sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type)

dutchprofile = DutchProfile(codespace, data_source, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set_financier, responsibility_set_partitie],
                                                 organisations=[operator], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type], zones=[transport_administrative_zone_partitie])

line = Line(id=getId(Line, codespace, "MOJO"), version=version.version, name=MultilingualString(value="MOJO"),
              monitored=False,
              responsibility_set_ref_attribute=responsibility_set_financier.id,
              description=MultilingualString(value="Festival vervoer Rammstein"),
              transport_mode=AllVehicleModesOfTransportEnumeration.BUS,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="MOJO"),
              private_code=PrivateCode(value="1", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "MOJO"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.UNKNOWN)
              )


rp_n = RoutePoint(id=getId(RoutePoint, codespace, "N"), version=version.version, location=LocationStructure2(pos=Pos(value=[187126, 428463], srs_dimension=2)))
rp_g = RoutePoint(id=getId(RoutePoint, codespace, "G"), version=version.version, location=LocationStructure2(pos=Pos(value=[186006, 426725], srs_dimension=2)))

route_points = [rp_n, rp_g]

rl_ng = RouteLink(id=getId(RouteLink, codespace, "N-G"), version=version.version,
                  distance=Decimal('3500'), # TODO
                  from_point_ref=getRef(rp_n, RoutePointRefStructure), to_point_ref=getRef(rp_g, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "N-G").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_n.location.pos.value + rp_g.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_gn = RouteLink(id=getId(RouteLink, codespace, "G-N"), version=version.version,
                distance=Decimal('3500'), # TODO
                    from_point_ref=getRef(rp_g, RoutePointRefStructure), to_point_ref=getRef(rp_n, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "G-N").replace(":", "_").replace("-", "_"),
                        pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=rp_g.location.pos.value + rp_n.location.pos.value)]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_ng, rl_gn]



route_ng = Route(id=getId(Route, codespace, "N-G"), version=version.version,
                 distance=Decimal('3500'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "N-G-N"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_n), onward_route_link_ref=getRef(rl_ng, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "N-G-G"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_g)),
                   ])
                   )

route_gn = Route(id=getId(Route, codespace, "G-N"), version=version.version,
                 distance=Decimal('3500'), # TODO
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "G-N-G"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_g), onward_route_link_ref=getRef(rl_gn, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "G-N-N"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_n)),
                   ])
                   )

routes = [route_ng, route_gn]

lines = [line]

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_n = DestinationDisplay(id=getId(DestinationDisplay, codespace, "N"), version=version.version,
                           name=MultilingualString(value="Centraal Station"),
                           front_text=MultilingualString(value="Centraal Station"),
                           private_code=PrivateCode(value="1", type_value="DestinationCode"))
setVariants(dd_n)

dd_g = DestinationDisplay(id=getId(DestinationDisplay, codespace, "G"), version=version.version,
                           name=MultilingualString(value="Rammstein"),
                           front_text=MultilingualString(value="Rammstein"),
                           private_code=PrivateCode(value="2", type_value="DestinationCode"))
setVariants(dd_g)


destination_displays=[dd_n, dd_g]

sa_n = StopArea(id=getId(StopArea, codespace, "N"),
                 version=version.version,
                 name=MultilingualString(value="Centraal Station"),
                 private_code=PrivateCode(value="60001002", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Nijmegen"))
                 )

sa_g = StopArea(id=getId(StopArea, codespace, "G"),
                 version=version.version,
                 name=MultilingualString(value="Festival"),
                 private_code=PrivateCode(value="60000001", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Nijmegen"))
                 )

stop_areas=[sa_n, sa_g]

ssp_n = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "N"), version=version.version,
                              name=MultilingualString(value="Centraal Station"),
                              location=LocationStructure2(pos=Pos(value=[187126, 428463], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "N"), version=version.version, project_to_point_ref=getRef(rp_n, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_n)]),
                              private_code=PrivateCode(value="60001002", type_value="UserStopCode"))

ssp_g = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "G"), version=version.version,
                              name=MultilingualString(value="Festival"),
                              location=LocationStructure2(pos=Pos(value=[186006, 426725], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "G"), version=version.version, project_to_point_ref=getRef(rp_g, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_g)]),
                              private_code=PrivateCode(value="60000001", type_value="UserStopCode"))


scheduled_stop_points=[ssp_n, ssp_g]

tl_ng = TimingLink(id=getId(TimingLink, codespace, "N-G"), version=version.version,
                   distance=Decimal('3500'), # TODO
                   from_point_ref=getRef(ssp_n, TimingPointRefStructure), to_point_ref=getRef(ssp_g, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_gn = TimingLink(id=getId(TimingLink, codespace, "G-N"), version=version.version,
                   distance=Decimal('3500'), #TODO
                   from_point_ref=getRef(ssp_g, TimingPointRefStructure), to_point_ref=getRef(ssp_n, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

timing_links = [tl_ng, tl_gn]


stop_assignments=[PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "N"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_n),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:60001002", QuayRef, "any")), # TODO
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "G"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_g),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:60000001", QuayRef, "any"))]

sjp_ng = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "N-G"), version=version.version,
                                 route_ref_or_route_view=getRef(route_ng),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_g),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "N-G-N"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_n),
                                                                   onward_timing_link_ref=getRef(tl_ng, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "N-G-G"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_g)),
                                     ]
                                    )
                                 )

sjp_gn = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "G-N"), version=version.version,
                                 route_ref_or_route_view=getRef(route_gn),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_n),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "G-N-G"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_g),
                                                                   onward_timing_link_ref=getRef(tl_gn, TimingLinkRefStructure),
                                                                   is_wait_point=False),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "G-N-N"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_n)),
                                     ]
                                    )
                                 )


journey_patterns=[sjp_ng, sjp_gn]

tdt_ng = TimeDemandType(id=getId(TimeDemandType, codespace, "N-G"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "N-G"), version=version.version, timing_link_ref=getRef(tl_ng), run_time=XmlDuration("PT480S"))]))

tdt_gn = TimeDemandType(id=getId(TimeDemandType, codespace, "G-N"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "G-N"), version=version.version, timing_link_ref=getRef(tl_gn), run_time=XmlDuration("PT480S"))]))

time_demand_types=[tdt_ng, tdt_gn]

service_frames = dutchprofile.getServiceFrames(route_points=route_points, route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=scheduled_stop_points, stop_areas=stop_areas,
                                              stop_assignments=stop_assignments, timing_points=None, timing_links=timing_links, service_journey_patterns=journey_patterns, time_demand_types=time_demand_types,
                                              notices=None, notice_assignments=None)


timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions, operator_view=OperatorView(operator_ref=getRef(operator)), vehicle_journeys=service_journeys)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[codespace], versions=[version],
                                                 responsibility_set=responsibility_set_partitie,
                                                 resource_frames=resource_frames, service_frames=service_frames, timetable_frames=timetable_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste MOJO export")

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