import sqlite3
from typing import Generator

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from netex import PublicationDelivery, ParticipantRef, MultilingualString, DataObjectsRelStructure, GeneralFrame, \
    GeneralFrameMembersRelStructure, ServiceJourney, StopPlace, CompositeFrame, FramesRelStructure, TimetableFrame, \
    JourneysInFrameRelStructure, TypeOfFrame, TypeOfFrameRef, ServiceFrame, JourneyPatternsInFrameRelStructure, \
    DirectionsInFrameRelStructure, ServiceJourneyPattern, Direction, RoutePointsInFrameRelStructure, RoutePoint, \
    ScheduledStopPointsInFrameRelStructure, ScheduledStopPoint, RoutesInFrameRelStructure, Route, \
    LinesInFrameRelStructure, Line, SiteFrame, ResourceFrame, CodespacesRelStructure, Codespace, \
    StopPlacesInFrameRelStructure, ServiceFacilitySet, DataSourcesInFrameRelStructure, OrganisationsInFrameRelStructure, \
    VehicleTypesInFrameRelStructure, ResponsibilitySetsInFrameRelStructure, DataSource, Authority, Operator, \
    VehicleType, ResponsibilitySet, Branding, RouteLinksInFrameRelStructure, RouteLink, Network, \
    NetworksInFrameRelStructure, DestinationDisplaysInFrameRelStructure, DestinationDisplay, \
    ServiceLinksInFrameRelStructure, ServiceLink, TransfersInFrameRelStructure, StopAssignmentsInFrameRelStructure, \
    PassengerStopAssignment, Connection, SiteConnection, DefaultConnection, ServiceCalendarFrame, \
    DayTypesInFrameRelStructure, ServiceCalendar, DayType, FlexibleLine

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config)

context = XmlContext()
config = ParserConfig(fail_on_unknown_properties=False)
parser = XmlParser(context=context, config=config, handler=LxmlEventHandler)

def load_generator(con, clazz, limit=None):
    type = getattr(clazz.Meta, 'name', clazz.__name__)

    cur = con.cursor()
    try:
        if limit is None:
            cur.execute(f"SELECT object FROM {type};")
        else:
            cur.execute(f"SELECT object FROM {type} LIMIT {limit};")
    except sqlite3.OperationalError:
        return None

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        yield parser.from_bytes(xml[0], clazz)

def chain(*iterables) -> Generator:
    for it in iterables:
        for element in it:
            yield element

def dontsetifnone(clazz, attr, value):
    if value is None:
        return None

    try:
        first = value.__next__()
    except StopIteration:
        return None
    else:
        return clazz(**{attr: chain([first],value)})

class GeneratorTester:
    def __init__(self, value):
        self._has_value = None
        self.value = value

    def has_value(self):
        if self._has_value is not None:
            return self._has_value

        try:
            self.first = self.value.__next__()
            self._has_value = True
        except StopIteration:
            self._has_value = False
            pass

        return self._has_value

    def generator(self):
        if self._has_value is None:
            return self.value

        elif self._has_value:
            return chain([self.first], self.value)

        return None

with sqlite3.connect("/tmp/target.sqlite") as con:
    codespace_ref_or_codespace = GeneratorTester(load_generator(con, Codespace))
    data_source = GeneratorTester(load_generator(con, DataSource))
    organisation_or_transport_organisation = GeneratorTester(chain(load_generator(con, Authority), load_generator(con, Operator)))
    transport_type_dummy_type_or_train_type = GeneratorTester(load_generator(con, VehicleType))
    responsibility_set = GeneratorTester(load_generator(con, ResponsibilitySet))

    stop_place = GeneratorTester(load_generator(con, StopPlace))

    direction = GeneratorTester(load_generator(con, Direction))
    route_point = GeneratorTester(load_generator(con, RoutePoint))
    route_link = GeneratorTester(load_generator(con, RouteLink))
    route = GeneratorTester(load_generator(con, Route))
    line = GeneratorTester(chain(load_generator(con, Line), load_generator(con, FlexibleLine)))
    destination_display = GeneratorTester(load_generator(con, DestinationDisplay))
    scheduled_stop_point = GeneratorTester(load_generator(con, ScheduledStopPoint))
    service_link = GeneratorTester(load_generator(con, ServiceLink))
    journey_pattern = GeneratorTester(load_generator(con, ServiceJourneyPattern))
    transfer = GeneratorTester(chain(load_generator(con, Connection), load_generator(con, SiteConnection), load_generator(con, DefaultConnection)))
    stop_assignment = GeneratorTester(load_generator(con, PassengerStopAssignment))

    service_journey = GeneratorTester(load_generator(con, ServiceJourney, 10))

    day_type = GeneratorTester(load_generator(con, DayType))

publication_delivery = PublicationDelivery(
                version="ntx:1.1",
                publication_timestamp=XmlDateTime.now(),
                participant_ref=ParticipantRef(value="NDOV"),
                description=MultilingualString(value="Huge XML Serializer test"),
                data_objects=DataObjectsRelStructure(choice=[
                    CompositeFrame(
                        type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_NETWORK_OFFER', version_ref='1.0'),
                        codespaces=CodespacesRelStructure(codespace_ref_or_codespace=codespace_ref_or_codespace.generator()) if codespace_ref_or_codespace.has_value() else None,
                        frames=FramesRelStructure(
                            common_frame=[
                                ResourceFrame(
                                    type_of_frame_ref=TypeOfFrameRef(ref='epip:COMMON', version_ref='1.0'),
                                    data_sources=DataSourcesInFrameRelStructure(data_source=data_source.generator()) if data_source.has_value() else None,
                                    organisations=OrganisationsInFrameRelStructure(organisation_or_transport_organisation=organisation_or_transport_organisation.generator()) if organisation_or_transport_organisation.has_value() else None,
                                    vehicle_types=VehicleTypesInFrameRelStructure(transport_type_dummy_type_or_train_type=transport_type_dummy_type_or_train_type.generator()) if transport_type_dummy_type_or_train_type.has_value() else None,
                                    responsibility_sets=ResponsibilitySetsInFrameRelStructure(responsibility_set=responsibility_set.generator()) if responsibility_set.has_value() else None,
                                    # brandings=BrandingsInFrameRelStructure(branding=load_generator(con, Branding)) # TODO: must be added to a ValueSet
                                ),

                                SiteFrame(
                                     type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_STOP', version_ref='1.0'),
                                     stop_places=StopPlacesInFrameRelStructure(stop_place=stop_place.generator()) if stop_place.has_value() else None,
                                ),

                                ServiceFrame(
                                     type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_NETWORK', version_ref='1.0'),
                                     directions=DirectionsInFrameRelStructure(direction=direction.generator()) if direction.has_value() else None,
                                     route_points=RoutePointsInFrameRelStructure(route_point=route_point.generator()) if route_point.has_value() else None,
                                     route_links=RouteLinksInFrameRelStructure(route_link=route_link.generator()) if route_link.has_value() else None,
                                     routes=RoutesInFrameRelStructure(route=route.generator()) if route.has_value() else None,
                                     lines=LinesInFrameRelStructure(line=line.generator()) if line.has_value() else None,
                                     # network=list(load_generator(con, Network, 1))[0], # Warning; we must handle multiple stuff
                                     destination_displays=DestinationDisplaysInFrameRelStructure(destination_display=destination_display.generator()) if destination_display.has_value() else None,
                                     scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_point.generator()) if scheduled_stop_point.has_value() else None,
                                     service_links=ServiceLinksInFrameRelStructure(service_link=service_link.generator()) if service_link.has_value() else None,
                                     journey_patterns=JourneyPatternsInFrameRelStructure(journey_pattern=journey_pattern.generator()) if journey_pattern.has_value() else None,
                                     connections=TransfersInFrameRelStructure(transfer=transfer.generator()) if transfer.has_value() else None,
                                     stop_assignments=StopAssignmentsInFrameRelStructure(stop_assignment=stop_assignment.generator()) if stop_assignment.has_value() else None,
                                ),
                                TimetableFrame(
                                     type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_TIMETABLE', version_ref='1.0'),
                                     vehicle_journeys=JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=service_journey.generator()) if service_journey.has_value() else None,
                                ),
                                ServiceCalendarFrame(
                                     type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_CALENDAR', version_ref='1.0'),
                                     day_types=DayTypesInFrameRelStructure(day_type=day_type.generator()) if day_type.has_value() else None,
                                     service_calendar=list(load_generator(con, ServiceCalendar, 1))[0], # Warning; we must handle multiple stuff
                                ),
                            ]
                        )
                    )
                ]))

ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}
with open('netex-output/huge.xml', 'w') as out:
    serializer.write(out, publication_delivery, ns_map)