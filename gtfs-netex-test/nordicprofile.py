from typing import List, Dict

from xsdata.models.datatype import XmlDateTime

import utils
from netex import Codespace, DataSource, Version, VehicleJourney, TimetableFrame, ServiceJourney, ServiceJourneyPattern, \
    ServiceFrame, ResourceFrame, PublicationDelivery, Line, MultilingualString, DataObjectsRelStructure, \
    JourneysInFrameRelStructure, JourneyPattern, DeadRunJourneyPattern, ServiceJourneyPatternRef, JourneyPatternRef, \
    Route, JourneyPatternsInFrameRelStructure, RoutesInFrameRelStructure, LinesInFrameRelStructure, \
    TimetabledPassingTimesRelStructure, Operator, OrganisationsInFrameRelStructure, ServiceCalendarFrame, \
    DataSourcesInFrameRelStructure, DayTypesInFrameRelStructure, DayTypeAssignment, DayType, \
    DayTypeAssignmentsInFrameRelStructure, RoutePointsInFrameRelStructure, DestinationDisplaysInFrameRelStructure, \
    ScheduledStopPointsInFrameRelStructure, TimingPointsInFrameRelStructure, TimingLinksInFrameRelStructure, \
    ServiceLinksInFrameRelStructure, StopAssignmentsInFrameRelStructure, Network, GroupsOfLinesInFrameRelStructure, \
    GroupOfLines
from refs import getRef, getIndex
from timetabledpassingtimesprofile import TimetablePassingTimesProfile


class NordicProfile:
    codespace: Codespace
    data_source: DataSource
    version: Version

    def __init__(self, codespace: Codespace, data_source: DataSource, version: Version):
        self.codespace = codespace
        self.data_source = data_source
        self.version = version


    @staticmethod
    def projectServiceJourneyPattern(service_journey_pattern: ServiceJourneyPattern) -> JourneyPattern:
        journey_pattern: JourneyPattern = utils.project(service_journey_pattern, JourneyPattern)
        return journey_pattern

    @staticmethod
    def projectDeadRunJourneyPattern(dead_run_journey_pattern: DeadRunJourneyPattern) -> JourneyPattern:
        journey_pattern: JourneyPattern = utils.project(dead_run_journey_pattern, JourneyPattern)
        return journey_pattern

    @staticmethod
    def projectNetworkFromLines(lines: List[Line]) -> Network:
        group_of_lines: GroupOfLines = GroupOfLines(id="GroupOfLines", name=MultilingualString(value="GroupOfLines"))
        ref = getRef(group_of_lines)
        for line in lines:
            line.represented_by_group_ref = ref

        network: Network = Network(id="Network", groups_of_lines=GroupsOfLinesInFrameRelStructure(group_of_lines=[group_of_lines]))
        return network

    @staticmethod
    def getServiceJourney(service_journey: ServiceJourney, journey_patterns: Dict[str, object]):
        journey_pattern: JourneyPattern = None

        if service_journey.journey_pattern_ref is None:
            # create JourneyPattern from calls or passingtimes
            pass

        else:
            if isinstance(service_journey.journey_pattern_ref, ServiceJourneyPatternRef):
                service_journey_pattern: ServiceJourneyPattern = journey_patterns.get(service_journey.journey_pattern_ref.ref, None)
                journey_pattern = NordicProfile.projectServiceJourneyPattern(service_journey_pattern)
                journey_patterns[journey_pattern.id] = journey_pattern
                service_journey.journey_pattern_ref = getRef(journey_pattern, JourneyPatternRef)

            elif isinstance(service_journey.journey_pattern_ref, JourneyPatternRef):
                # NO-OP, this is what the profile wants
                pass

            else:
                print("Unhandled input")

        if service_journey.passing_times is None:
            if service_journey.calls is not None:
                ttpt = TimetablePassingTimesProfile.getTimetabledPassingtimesFromCalls(service_journey, journey_pattern)
                if len(ttpt) > 0:
                    service_journey.passing_times = TimetabledPassingTimesRelStructure(timetabled_passing_time=ttpt)
                    service_journey.calls = None

        # service_journey.validity_conditions_or_valid_between = None

        return service_journey

    def getDataSources(self, data_sources: List[DataSource]) -> List[DataSource]:
        return data_sources

    def getServiceFrameShared(self, network, route_points, destination_displays, scheduled_stop_points, timing_points, timing_links, service_links, stop_assignments):
        if len(route_points) > 0:
            route_points = RoutePointsInFrameRelStructure(route_point=route_points)
        else:
            route_points = None

        if len(destination_displays) > 0:
            destination_displays = DestinationDisplaysInFrameRelStructure(destination_display=destination_displays)
        else:
            destination_displays = None

        if len(scheduled_stop_points) > 0:
            scheduled_stop_points = ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_points)
        else:
            scheduled_stop_points = None

        if len(timing_points) > 0:
            timing_points = TimingPointsInFrameRelStructure(timing_point=timing_points)
        else:
            timing_points = None

        if len(timing_links) > 0:
            timing_links = TimingLinksInFrameRelStructure(timing_link=timing_links)
        else:
            timing_links = None

        if len(service_links) > 0:
            service_links = ServiceLinksInFrameRelStructure(service_link=service_links)
        else:
            service_links = None

        if len(stop_assignments) > 0:
            stop_assignments = StopAssignmentsInFrameRelStructure(stop_assignment=stop_assignments)
        else:
            stop_assignments = None

        service_frame = ServiceFrame(id="ServiceFrame", version=self.version.version,
                                     network=network,
                                     route_points=route_points,
                                     destination_displays=destination_displays,
                                     scheduled_stop_points=scheduled_stop_points,
                                     timing_points=timing_points,
                                     timing_links=timing_links,
                                     service_links=service_links,
                                     stop_assignments=stop_assignments
                                     )
        return service_frame

    def getServiceCalendarFrameShared(self, day_types: List[DayType], day_type_assignments: List[DayTypeAssignment]):
        if len(day_type_assignments) > 0:
            day_type_assignments = DayTypeAssignmentsInFrameRelStructure(day_type_assignment=day_type_assignments)
        else:
            day_type_assignments = None

        if len(day_types) > 0:
            day_types = DayTypesInFrameRelStructure(day_type=day_types)
        else:
            day_types = None

        service_calendar_frame = ServiceCalendarFrame(id="ServiceCalendarFrame", version=self.version.version,
                                                      day_type_assignments=day_type_assignments,
                                                      day_types=day_types)

        return service_calendar_frame

    def getResourceFrameShared(self, operators: List[Operator]) -> ResourceFrame:
        resource_frame = ResourceFrame(id="ResourceFrame", version="1",
                                       data_sources=DataSourcesInFrameRelStructure(data_source=[self.data_source]),
                                       organisations=OrganisationsInFrameRelStructure(organisation_or_transport_organisation=operators))
        return resource_frame



    def getShared(self, resource_frame: List[ResourceFrame], service_frame: List[ServiceFrame], service_calendar_frame: List[ServiceCalendarFrame]) -> PublicationDelivery:
        return PublicationDelivery(version="1.08:NO-NeTEx-networktimetable:1.3",
                                   publication_timestamp=XmlDateTime.now(),
                                   participant_ref="PyNeTExConv",
                                   description=MultilingualString(value="Export"),
                                   data_objects=DataObjectsRelStructure(
                                       choice=resource_frame + service_frame + service_calendar_frame)
                                   )

    def getTimetableFrame(self, line: Line, service_journeys: List[ServiceJourney], journey_patterns: List[object]) -> TimetableFrame:
        journey_patterns_index = getIndex(journey_patterns, 'id')
        [NordicProfile.getServiceJourney(service_journey, journey_patterns_index) for service_journey in service_journeys]

        # Make sure that all introduced journey patterns will be 'returned'
        journey_patterns.clear()
        journey_patterns += list(journey_patterns_index.values())

        return TimetableFrame(id=line.id.replace("Line", "TimetableFrame"), vehicle_journeys=JourneysInFrameRelStructure(choice=service_journeys))

    def getServiceFrame(self, line: Line, journey_patterns: List[JourneyPattern], routes: List[Route]) -> ServiceFrame:
        if len(routes) > 0:
            routes = RoutesInFrameRelStructure(route=routes)
        else:
            routes = None

        return ServiceFrame(id=line.id.replace("Line", "ServiceFrame"),
                            lines=LinesInFrameRelStructure(line=[line]),
                            journey_patterns=JourneyPatternsInFrameRelStructure(journey_pattern=journey_patterns),
                            routes=routes)

    def getLineDelivery(self, line: Line, resource_frame: [ResourceFrame], service_frame: [ServiceFrame], timetable_frame: [TimetableFrame]) -> PublicationDelivery:
        return PublicationDelivery(version="1.08:NO-NeTEx-networktimetable:1.3",
                                   publication_timestamp=XmlDateTime.now(),
                                   participant_ref="PyNeTExConv",
                                   description=line.description,
                                   data_objects=DataObjectsRelStructure(choice=resource_frame + service_frame + timetable_frame)
                                   )
