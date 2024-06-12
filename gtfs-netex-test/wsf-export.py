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

short_name = "WSF"

codespace = Codespace(id="{}:Codespace:{}".format("BISON", short_name), xmlns=short_name,
                      xmlns_url="http://bison.dova.nu/ns/WSF", description=MultilingualString(value="Westerschelde Ferry"))

dova_codespace = Codespace(id="{}:Codespace:{}".format("BISON", "DOVA"), xmlns="DOVA",
                      xmlns_url="http://bison.dova.nu/ns/DOVA", description=MultilingualString(value="'Centrale' lijsten bijgehouden door DOVA"))

start_date = datetime.datetime(year=2023, month=11, day=29)
end_date = datetime.datetime(year=2023, month=12, day=29)

today = str(datetime.date.today()).replace('-', '')

version = Version(id=getId(Version, codespace, today),
                  version=today,
                  start_date=XmlDateTime.from_datetime(start_date),
                  end_date=XmlDateTime.from_datetime(end_date),
                  version_type=VersionTypeEnumeration.BASELINE)

stt = SimpleTimetable(codespace, version)
from_date = datetime.date.today().isoformat().replace('-', '')
service_journeys, availability_conditions = stt.simple_timetable(f"../wsf/scrape-output/wsf-{from_date}.csv")

version.start_date = availability_conditions[0].from_date
version.end_date = availability_conditions[0].to_date

data_source = DataSource(id=getId(DataSource, codespace, short_name),
                         version=version.version,
                         name=MultilingualString(value=short_name),
                         short_name=MultilingualString(value=short_name),
                         description=MultilingualString(value=short_name))

transport_administrative_zone = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, dova_codespace, "FFVB"),
                                                            version="any",
                                                            name=MultilingualString(value="Fast Ferry Vlissingen-Breskens"),
                                                            short_name=MultilingualString(value="FFVB"),
                                                            vehicle_modes=[AllModesEnumeration.WATER])

transport_administrative_zone_partitie = TransportAdministrativeZone(id=getId(TransportAdministrativeZone, codespace, "WSF"),
                                                            version="any",
                                                            name=MultilingualString(value="Westerschelde Ferry"),
                                                            short_name=MultilingualString(value="WSF"),
                                                            vehicle_modes=[AllModesEnumeration.WATER])


operator = Operator(id=getId(Operator, codespace, "WSF"), version=version.version,
                        company_number="61547336",
                        name=MultilingualString(value="WSF"),
                        short_name=MultilingualString(value="WSF"),
                        legal_name=MultilingualString(value="Westerschelde Ferry B.V."),
                        organisation_type=[OrganisationTypeEnumeration.OPERATOR],
                        primary_mode=AllModesEnumeration.WATER,
                        contact_details=ContactStructure(url="https://westerscheldeferry.nl/"),
                        customer_service_contact_details=ContactStructure(email="info@westerscheldeferry.nl", phone="+31850401800", url="https://westerscheldeferry.nl/"),
                        operator_activities=[OperatorActivitiesEnumeration.PASSENGER])

authority = Authority(id=getId(Authority, dova_codespace, "ZLD"), version="any", name=MultilingualString(value="Zeeland"), short_name=MultilingualString(value="ZLD"), description=MultilingualString(value="Provincie Zeeland"))

responsibility_set_concessie = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, "Concessie"),
                                       version=version.version,
                                       name=MultilingualString(value="Concessie"),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(id=getId(ResponsibilityRoleAssignment, codespace, "Concessie"),
                                                                        version=version.version,
                                                                        responsible_area_ref=getRef(transport_administrative_zone, VersionOfObjectRefStructure))
                                       ]))

responsibility_set_financier = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, "Financier"),
                                       version=version.version,
                                       name=MultilingualString(value="Financier"),
                                       roles=ResponsibilityRoleAssignmentsRelStructure(responsibility_role_assignment=[
                                           ResponsibilityRoleAssignment(
                                               id=getId(ResponsibilityRoleAssignment, codespace, "Financier"),
                                               version=version.version,
                                               type_of_responsibility_role_ref_or_responsibility_role_ref=TypeOfResponsibilityRoleRef(ref="BISON:TypeOfResponsibilityRole:financing", version="any"),
                                               responsible_organisation_ref=getRef(authority, OrganisationRefStructure)),
                                       ]))

responsibility_set_partitie = ResponsibilitySet(id=getId(ResponsibilitySet, codespace, short_name),
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

vehicle_type = VehicleType(id=getId(VehicleType, codespace, "PMPWA"), version=version.version,
                           name=MultilingualString(value="Prinses Maxima en Prins Willem Alexander"),
                           description=MultilingualString(value="Prinses Maxima en Prins Willem Alexander"),
                           # fuel_type_or_type_of_fuel=TransportTypeVersionStructure.FuelType(value=[FuelTypeEnumeration.DIESEL]),
                           fuel_type_or_type_of_fuel=TransportTypeVersionStructure.TypeOfFuel(value=FuelTypeEnumeration.DIESEL),
                           capacities=PassengerCapacitiesRelStructure(passenger_capacity_ref_or_passenger_capacity_or_passenger_vehicle_capacity=
                                                                      [PassengerCapacity(id=getId(PassengerCapacity, codespace, "PMPWA"), version=version.version,
                                                                          fare_class=FareClassEnumeration.ANY, total_capacity=186, seating_capacity=186)]),
                           length=Decimal(value='37.71'), width=Decimal(value='17.31'), height=Decimal(value='4.20'),
                           transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
                           has_lift_or_ramp=False,
                           low_floor=True,
                           facilities=ServiceFacilitySetsRelStructure(
                               service_facility_set_ref_or_service_facility_set=
                               [ServiceFacilitySet(id=getId(ServiceFacilitySet, codespace, "PMPWA"), version=version.version,
                                                  mobility_facility_list=MobilityFacilityList(value=[MobilityFacilityEnumeration.SUITABLE_FOR_WHEELCHAIRS]),
                                                  ticketing_service_facility_list=TicketingServiceFacilityList(value=[TicketingServiceFacilityEnumeration.PURCHASE, TicketingServiceFacilityEnumeration.RESERVATIONS]),
                                                   vehicle_access_facility_list=VehicleAccessFacilityList(value=[VehicleAccessFacilityEnumeration.AUTOMATIC_RAMP]),
                                                  sanitary_facility_list=SanitaryFacilityList(value=[SanitaryFacilityEnumeration.TOILET, SanitaryFacilityEnumeration.WHEELCHAIR_ACCESS_TOILET, SanitaryFacilityEnumeration.BABY_CHANGE]),
                                                  )]
                           ))

sj: ServiceJourney
for sj in service_journeys:
    sj.compound_train_ref_or_train_ref_or_vehicle_type_ref = getRef(vehicle_type)

dutchprofile = DutchProfile(codespace, data_source, version)
resource_frames = dutchprofile.getResourceFrames(data_sources=[data_source], responsibility_sets=[responsibility_set_concessie, responsibility_set_financier, responsibility_set_partitie],
                                                 organisations=[operator, authority], operational_contexts=[operational_context],
                                                 vehicle_types=[vehicle_type], zones=[transport_administrative_zone_partitie])

line = Line(id=getId(Line, codespace, "WSF"), version=version.version, name=MultilingualString(value="WSF"),
              monitored=False,
              responsibility_set_ref_attribute=responsibility_set_concessie.id,
              description=MultilingualString(value="Veer tussen Vlissingen en Breskens"),
              transport_mode=AllVehicleModesOfTransportEnumeration.WATER,
              type_of_service_ref=TypeOfServiceRef(ref="BISON:TypeOfService:Standaard", version="any"),
              public_code=PublicCodeStructure(value="WSF"),
              private_code=PrivateCode(value="1", type_value="LinePlanningNumber"),
              accessibility_assessment=AccessibilityAssessment(id=getId(AccessibilityAssessment, codespace, "WSF"), version=version.version,
                                                               mobility_impaired_access=LimitationStatusEnumeration.TRUE)
              )


rp_v = RoutePoint(id=getId(RoutePoint, codespace, "V"), version=version.version, location=LocationStructure2(pos=Pos(value=[30576, 385411], srs_dimension=2)))
rp_b = RoutePoint(id=getId(RoutePoint, codespace, "B"), version=version.version, location=LocationStructure2(pos=Pos(value=[27072, 380785], srs_dimension=2)))

route_points = [rp_v, rp_b]

rl_vb = RouteLink(id=getId(RouteLink, codespace, "V-B"), version=version.version,
                  distance=Decimal('5803'),
                  from_point_ref=getRef(rp_v, RoutePointRefStructure), to_point_ref=getRef(rp_b, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "V-B").replace(":", "_").replace("-", "_"),
                                           pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=(rp_v.location.pos.value + rp_b.location.pos.value))]),
                    operational_context_ref=getRef(operational_context))

rl_bv = RouteLink(id=getId(RouteLink, codespace, "B-V"), version=version.version,
                distance=Decimal('5803'),
                    from_point_ref=getRef(rp_b, RoutePointRefStructure), to_point_ref=getRef(rp_v, RoutePointRefStructure),
                    line_string=LineString(id=getId(RouteLink, codespace, "B-V").replace(":", "_").replace("-", "_"),
                        pos_or_point_property_or_pos_list=[PosList(srs_dimension=2, count=2, value=rp_b.location.pos.value + rp_v.location.pos.value)]),
                    operational_context_ref=getRef(operational_context))

route_links = [rl_vb, rl_bv]



route_vb = Route(id=getId(Route, codespace, "V-B"), version=version.version,
                 distance=Decimal('5803'),
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.INBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "V-B-V"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_v), onward_route_link_ref=getRef(rl_vb, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "V-B-B"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_b)),
                   ])
                   )

route_bv = Route(id=getId(Route, codespace, "B-V"), version=version.version,
                 distance=Decimal('5803'),
                 line_ref=getRef(line),
                   direction_type=DirectionType(value=DirectionTypeEnumeration.OUTBOUND),
                   points_in_sequence=PointsOnRouteRelStructure(point_on_route=[
                       PointOnRoute(id=getId(PointOnRoute, codespace, "B-V-B"), version=version.version, order=1, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_b), onward_route_link_ref=getRef(rl_bv, RouteLinkRefStructure)),
                       PointOnRoute(id=getId(PointOnRoute, codespace, "B-V-V"), version=version.version, order=2, point_ref_or_infrastructure_point_ref_or_activation_point_ref_or_timing_point_ref_or_scheduled_stop_point_ref_or_parking_point_ref_or_relief_point_ref_or_route_point_ref=getRef(rp_v)),
                   ])
                   )

routes = [route_vb, route_bv]

lines = [line]

def setVariants(dd: DestinationDisplay):
    dd.variants = DestinationDisplayVariantsRelStructure(destination_display_variant=[DestinationDisplayVariant(id=dd.id + "-" + str(x), version=dd.version, name=MultilingualString(value=dd.name.value[0:x]), destination_display_variant_media_type=DeliveryVariantTypeEnumeration.ANY, extensions=Extensions2(any_element=[AnyElement(qname="{http://www.netex.org.uk/netex}MaxLength", text="BISON:DisplayTextLength:"+str(x))])) for x in (24, 21, 19, 16)])

dd_v = DestinationDisplay(id=getId(DestinationDisplay, codespace, "V"), version=version.version,
                           name=MultilingualString(value="Vlissingen"),
                           front_text=MultilingualString(value="Vlissingen"),
                           private_code=PrivateCode(value="1", type_value="DestinationCode"))
setVariants(dd_v)

dd_b = DestinationDisplay(id=getId(DestinationDisplay, codespace, "B"), version=version.version,
                           name=MultilingualString(value="Breskens"),
                           front_text=MultilingualString(value="Breskens"),
                           private_code=PrivateCode(value="2", type_value="DestinationCode"))
setVariants(dd_b)


destination_displays=[dd_v, dd_b]

sa_v = StopArea(id=getId(StopArea, codespace, "V"),
                 version=version.version,
                 name=MultilingualString(value="Vlissingen"),
                 private_code=PrivateCode(value="1", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Vlissingen"))
                 )

sa_b = StopArea(id=getId(StopArea, codespace, "B"),
                 version=version.version,
                 name=MultilingualString(value="Breskens"),
                 private_code=PrivateCode(value="2", type_value="UserStopAreaCode"),
                 topographic_place_ref_or_topographic_place_view=TopographicPlaceView(name=MultilingualString(value="Breskens"))
                 )

stop_areas=[sa_v, sa_b]

ssp_v = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "V"), version=version.version,
                              name=MultilingualString(value="Vlissingen, Westerhavenweg"),
                              location=LocationStructure2(pos=Pos(value=[30576, 385411], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "V"), version=version.version, project_to_point_ref=getRef(rp_v, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_v)]),
                              private_code=PrivateCode(value="7660001", type_value="UserStopCode"))

ssp_b = ScheduledStopPoint(id=getId(ScheduledStopPoint, codespace, "B"), version=version.version,
                              name=MultilingualString(value="Breskens, Veerhaven"),
                              location=LocationStructure2(pos=Pos(value=[27072, 380785], srs_dimension=2)),
                              projections=ProjectionsRelStructure(projection_ref_or_projection=[PointProjection(id=getId(PointProjection, codespace, "B"), version=version.version, project_to_point_ref=getRef(rp_b, PointRefStructure))]),
                              for_alighting=True, for_boarding=True,
                              stop_areas=StopAreaRefsRelStructure(stop_area_ref=[getRef(sa_b)]),
                              private_code=PrivateCode(value="7960001", type_value="UserStopCode"))


scheduled_stop_points=[ssp_v, ssp_b]

tl_vb = TimingLink(id=getId(TimingLink, codespace, "V-B"), version=version.version,
                   distance=Decimal('5803'),
                   from_point_ref=getRef(ssp_v, TimingPointRefStructure), to_point_ref=getRef(ssp_b, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

tl_bv = TimingLink(id=getId(TimingLink, codespace, "B-V"), version=version.version,
                   distance=Decimal('5803'),
                   from_point_ref=getRef(ssp_b, TimingPointRefStructure), to_point_ref=getRef(ssp_v, TimingPointRefStructure),
                    operational_context_ref=getRef(operational_context))

timing_links = [tl_vb, tl_bv]


stop_assignments=[PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "V"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_v),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:76600010", QuayRef, "any")),
                  PassengerStopAssignment(id=getId(PassengerStopAssignment, codespace, "B"), version=version.version, order=1,
                                          fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point=getRef(ssp_b),
                                          taxi_stand_ref_or_quay_ref_or_quay=getFakeRef("NL:CHB:Quay:79600015", QuayRef, "any"))]

sjp_dhtx = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "V-B"), version=version.version,
                                 route_ref_or_route_view=getRef(route_vb),
                                 direction_type=DirectionTypeEnumeration.INBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_b),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "V-B-V"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_v),
                                                                   onward_timing_link_ref=getRef(tl_vb, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "V-B-B"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_b)),
                                     ]
                                    )
                                 )

sjp_txdh = ServiceJourneyPattern(id=getId(ServiceJourneyPattern, codespace, "B-V"), version=version.version,
                                 route_ref_or_route_view=getRef(route_bv),
                                 direction_type=DirectionTypeEnumeration.OUTBOUND,
                                 destination_display_ref_or_destination_display_view=getRef(dd_v),
                                 points_in_sequence=PointsInJourneyPatternRelStructure(
                                     point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern=[
                                         StopPointInJourneyPattern(id=getId(StopPointInJourneyPattern, codespace, "B-V-B"), version=version.version, order=1,
                                                                   scheduled_stop_point_ref=getRef(ssp_b),
                                                                   onward_timing_link_ref=getRef(tl_bv, TimingLinkRefStructure),
                                                                   is_wait_point=True),
                                         StopPointInJourneyPattern(
                                             id=getId(StopPointInJourneyPattern, codespace, "B-V-V"),
                                             version=version.version, order=2,
                                             scheduled_stop_point_ref=getRef(ssp_v)),
                                     ]
                                    )
                                 )


journey_patterns=[sjp_dhtx, sjp_txdh]

tdt_vb = TimeDemandType(id=getId(TimeDemandType, codespace, "V-B"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "V-B"), version=version.version, timing_link_ref=getRef(tl_vb), run_time=XmlDuration("PT1380S"))]))

tdt_bv = TimeDemandType(id=getId(TimeDemandType, codespace, "B-V"), version=version.version,
                          run_times=JourneyRunTimesRelStructure(journey_run_time=[JourneyRunTime(id=getId(JourneyRunTime, codespace, "B-V"), version=version.version, timing_link_ref=getRef(tl_bv), run_time=XmlDuration("PT1380S"))]))

time_demand_types=[tdt_vb, tdt_bv]

service_frames = dutchprofile.getServiceFrames(route_points=route_points, route_links=route_links, routes=routes, lines=lines,
                                               destination_displays=destination_displays, scheduled_stop_points=scheduled_stop_points, stop_areas=stop_areas,
                                              stop_assignments=stop_assignments, timing_points=None, timing_links=timing_links, service_journey_patterns=journey_patterns, time_demand_types=time_demand_types,
                                              notices=None, notice_assignments=None)


timetable_frames = dutchprofile.getTimetableFrame(content_validity_conditions=availability_conditions, operator_view=OperatorView(operator_ref=getRef(operator)), vehicle_journeys=service_journeys)

composite_frame = dutchprofile.getCompositeFrame(codespaces=[codespace], versions=[version],
                                                 responsibility_set=responsibility_set_partitie,
                                                 resource_frames=resource_frames, service_frames=service_frames, timetable_frames=timetable_frames)
publication_delivery = dutchprofile.getPublicationDelivery(composite_frame=composite_frame, description="Eerste WSF export")

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

from isal import igzip_threaded
import gzip
ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
with igzip_threaded.open(f"/tmp/NeTEx_WSF_WSF_{from_date}_{from_date}.xml.gz", 'wt', compresslevel=3, threads=3, block_size=2*10**8) as out:
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