import duckdb as sqlite3
from datetime import datetime, date
from typing import Generator
from utils import project
from isal import igzip_threaded

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.parsers.handlers import LxmlEventHandler
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter

from netexio.dbaccess import load_local
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
    DayTypesInFrameRelStructure, ServiceCalendar, DayType, FlexibleLine, VersionFrameDefaultsStructure, SystemOfUnits, \
    LocaleStructure, Notice, NoticeAssignment, NoticesInFrameRelStructure, NoticeAssignmentsInFrameRelStructure, \
    TopographicPlacesInFrameRelStructure, TopographicPlace, TransportOrganisationVersionStructure, Locale, \
    TypesOfValueInFrameRelStructure, ValueSet, ValidityConditionsRelStructure, AvailabilityCondition, JourneyMeeting, InterchangeRule, JourneyMeetingsInFrameRelStructure, InterchangeRulesInFrameRelStructure

import netex_monkeypatching

serializer_config = SerializerConfig(ignore_default_attributes=True, xml_declaration=True)
serializer_config.pretty_print = True
serializer_config.ignore_default_attributes = True
serializer = XmlSerializer(config=serializer_config, writer=XmlEventWriter)

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
    except sqlite3.duckdb.InvalidInputException:
        return None

    while True:
        xml = cur.fetchone()
        if xml is None:
            break
        if isinstance(xml[0], str):
            yield parser.from_string(xml[0], clazz)
        else:
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

    def has_value(self) -> bool:
        if self._has_value is not None:
            return self._has_value

        try:
            self.first = self.value.__next__()
            self._has_value = True
        except StopIteration:
            self._has_value = False
            pass

        return self._has_value

    def generator(self) -> Generator | None:
        if self._has_value is None:
            return self.value

        elif self._has_value:
            return chain([self.first], self.value)

        return None

def export_epip_network_offer(database_original, database_target, output_filename: str):
    # The way how con_orig, and con_target have been modelled, is too hardcoded.
    # An alternative would be to put all the contents in the con_target.

    con_orig = sqlite3.connect(database_original, read_only=True)
    con_target = sqlite3.connect(database_target, read_only=True)

    codespace_ref_or_codespace = GeneratorTester(load_generator(con_orig, Codespace))
    data_source = GeneratorTester(load_generator(con_orig, DataSource))
    organisation_or_transport_organisation = load_local(con_orig, Authority) + load_local(con_orig, Operator)
    value_set = GeneratorTester(load_generator(con_orig, ValueSet))

    all_locales = {org.locale for org in organisation_or_transport_organisation if org.locale is not None}
    if len(all_locales) > 1:
        print("TODO: Test case for multiple TimetableFrames!")

    transport_type_dummy_type_or_train_type = GeneratorTester(load_generator(con_orig, VehicleType))
    responsibility_set = GeneratorTester(load_generator(con_orig, ResponsibilitySet))

    stop_place = GeneratorTester(load_generator(con_target, StopPlace))
    topographic_place = GeneratorTester(load_generator(con_orig, TopographicPlace))

    direction = GeneratorTester(load_generator(con_target, Direction))
    route_point = GeneratorTester(load_generator(con_target, RoutePoint))
    route_link = GeneratorTester(load_generator(con_target, RouteLink))
    route = GeneratorTester(load_generator(con_orig, Route))
    line = GeneratorTester(chain(load_generator(con_target, Line), load_generator(con_orig, FlexibleLine)))
    network = GeneratorTester(load_generator(con_orig, Network, 1))
    destination_display = GeneratorTester(load_generator(con_orig, DestinationDisplay))
    scheduled_stop_point = GeneratorTester(load_generator(con_target, ScheduledStopPoint))
    service_link = GeneratorTester(load_generator(con_target, ServiceLink))
    journey_pattern = GeneratorTester(load_generator(con_target, ServiceJourneyPattern))
    transfer = GeneratorTester(chain(load_generator(con_target, Connection), load_generator(con_target, SiteConnection), load_generator(con_target, DefaultConnection)))
    stop_assignment = GeneratorTester(load_generator(con_target, PassengerStopAssignment))
    notice = GeneratorTester(load_generator(con_orig, Notice))
    notice_assignment = GeneratorTester(load_generator(con_orig, NoticeAssignment))

    journey_meeting = GeneratorTester(load_generator(con_orig, JourneyMeeting))
    interchange_rule = GeneratorTester(load_generator(con_orig, InterchangeRule))

    availability_condition = GeneratorTester(load_generator(con_orig, AvailabilityCondition))
    service_journey = GeneratorTester(load_generator(con_target, ServiceJourney))

    day_type = GeneratorTester(load_generator(con_target, DayType))
    service_calendar = GeneratorTester(load_generator(con_target, ServiceCalendar, 1))

    version = date.today().strftime("%Y%m%d")


    default_locale: LocaleStructure = project(list(all_locales)[0], LocaleStructure) if len(all_locales) > 0 else None
    if default_locale is not None and default_locale.languages is not None and len(default_locale.languages.language_usage) == 1:
        default_locale.default_language = default_locale.languages.language_usage[0].language

    publication_delivery = PublicationDelivery(
                    version="ntx:1.1",
                    publication_timestamp=XmlDateTime.now(),
                    participant_ref=ParticipantRef(value="NDOV"),
                    description=MultilingualString(value="Huge XML Serializer test"),
                    data_objects=DataObjectsRelStructure(choice=[
                        CompositeFrame(
                            id="EU_PI_NETWORK_OFFER", version=version,
                            type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_NETWORK_OFFER', version_ref='1.0'),
                            frame_defaults=VersionFrameDefaultsStructure(default_location_system="urn:ogc:def:crs:EPSG::4326",
                                                                         default_system_of_units=SystemOfUnits.SI_METRES,
                                                                         default_locale=default_locale
                                                                         ),
                            codespaces=CodespacesRelStructure(codespace_ref_or_codespace=codespace_ref_or_codespace.generator()) if codespace_ref_or_codespace.has_value() else None,
                            frames=FramesRelStructure(
                                common_frame=[
                                    ResourceFrame(
                                        id="COMMON", version=version,
                                        type_of_frame_ref=TypeOfFrameRef(ref='epip:COMMON', version_ref='1.0'),
                                        data_sources=DataSourcesInFrameRelStructure(data_source=data_source.generator()) if data_source.has_value() else None,
                                        types_of_value=TypesOfValueInFrameRelStructure(choice=value_set.generator()) if value_set.has_value() else None,
                                        organisations=OrganisationsInFrameRelStructure(organisation_or_transport_organisation=organisation_or_transport_organisation) if len(organisation_or_transport_organisation) > 0 else None,
                                        vehicle_types=VehicleTypesInFrameRelStructure(transport_type_dummy_type_or_train_type=transport_type_dummy_type_or_train_type.generator()) if transport_type_dummy_type_or_train_type.has_value() else None,
                                        responsibility_sets=ResponsibilitySetsInFrameRelStructure(responsibility_set=responsibility_set.generator()) if responsibility_set.has_value() else None,
                                        # brandings=BrandingsInFrameRelStructure(branding=load_generator(con, Branding)) # TODO: must be added to a ValueSet
                                    ),

                                    SiteFrame(
                                        id="EU_PI_STOP", version=version,
                                        type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_STOP', version_ref='1.0'),
                                        stop_places=StopPlacesInFrameRelStructure(stop_place=stop_place.generator()) if stop_place.has_value() else None,
                                        topographic_places=TopographicPlacesInFrameRelStructure(topographic_place=topographic_place.generator()) if topographic_place.has_value() else None,
                                    ),

                                    ServiceFrame(
                                        id="EU_PI_NETWORK", version=version,
                                        type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_NETWORK', version_ref='1.0'),
                                         directions=DirectionsInFrameRelStructure(direction=direction.generator()) if direction.has_value() else None,
                                         route_points=RoutePointsInFrameRelStructure(route_point=route_point.generator()) if route_point.has_value() else None,
                                         route_links=RouteLinksInFrameRelStructure(route_link=route_link.generator()) if route_link.has_value() else None,
                                         routes=RoutesInFrameRelStructure(route=route.generator()) if route.has_value() else None,
                                         lines=LinesInFrameRelStructure(line=line.generator()) if line.has_value() else None,
                                         network=list(network.generator())[0] if network.has_value() else None, # Warning; we must handle multiple stuff
                                         destination_displays=DestinationDisplaysInFrameRelStructure(destination_display=destination_display.generator()) if destination_display.has_value() else None,
                                         scheduled_stop_points=ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_point.generator()) if scheduled_stop_point.has_value() else None,
                                         service_links=ServiceLinksInFrameRelStructure(service_link=service_link.generator()) if service_link.has_value() else None,
                                         journey_patterns=JourneyPatternsInFrameRelStructure(journey_pattern=journey_pattern.generator()) if journey_pattern.has_value() else None,
                                         connections=TransfersInFrameRelStructure(transfer=transfer.generator()) if transfer.has_value() else None,
                                         stop_assignments=StopAssignmentsInFrameRelStructure(stop_assignment_or_passenger_boarding_position_assignment=stop_assignment.generator()) if stop_assignment.has_value() else None,
                                         notices=NoticesInFrameRelStructure(notice=notice.generator()) if notice.has_value() else None,
                                         notice_assignments=NoticeAssignmentsInFrameRelStructure(notice_assignment=notice_assignment.generator()) if notice_assignment.has_value() else None,
                                    ),
                                    TimetableFrame(
                                        id="EU_PI_TIMETABLE", version=version,
                                        type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_TIMETABLE', version_ref='1.0'),
                                        content_validity_conditions=ValidityConditionsRelStructure(choice=availability_condition.generator()) if availability_condition.has_value() else None,
                                        vehicle_journeys=JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=service_journey.generator()) if service_journey.has_value() else None,
                                        journey_meetings=JourneyMeetingsInFrameRelStructure(journey_meeting=journey_meeting.generator()) if journey_meeting.has_value() else None,
                                        interchange_rules=InterchangeRulesInFrameRelStructure(interchange_rule=interchange_rule.generator()) if interchange_rule.has_value() else None
                                    ),
                                    ServiceCalendarFrame(
                                        id="EU_PI_CALENDAR", version=version,
                                        type_of_frame_ref=TypeOfFrameRef(ref='epip:EU_PI_CALENDAR', version_ref='1.0'),
                                         day_types=DayTypesInFrameRelStructure(day_type=day_type.generator()) if day_type.has_value() else None,
                                         service_calendar=list(service_calendar.generator())[0] if service_calendar.has_value() else None, # Warning; we must handle multiple stuff
                                    ),
                                ]
                            )
                        )
                    ]))

    ns_map = {'': 'http://www.netex.org.uk/netex', 'gml': 'http://www.opengis.net/gml/3.2'}

    if output_filename.endswith('.gz'):
        with igzip_threaded.open(output_filename, 'wt', compresslevel=3, threads=3, block_size=2*10**8, encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)
    else:
        with open(output_filename, 'w', encoding='utf-8') as out:
            serializer.write(out, publication_delivery, ns_map)

if __name__ == '__main__':
    import argparse
    argument_parser = argparse.ArgumentParser(description='Export a prepared EPIP  import into DuckDB')
    argument_parser.add_argument('original', type=str, help='The original DuckDB NeTEx database')
    argument_parser.add_argument('target', type=str, help='The transformed DuckDB NeTEx database')
    argument_parser.add_argument('output', type=str, help='The NeTEx output filename, for example: netex.xml.gz')
    args = argument_parser.parse_args()

    export_epip_network_offer(args.original, args.target, args.output)
