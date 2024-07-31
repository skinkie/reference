from typing import List, Union

from xsdata.models.datatype import XmlDateTime

from netex import Codespace, VehicleScheduleFrame, Version, ServiceCalendarFrame, TimetableFrame, ServiceFrame, \
    ResourceFrame, CompositeFrame, FramesRelStructure, TypeOfFrameRef, VersionFrameDefaultsStructure, LocaleStructure, \
    SystemOfUnits, CodespaceRefStructure, DataSource, DataSourceRefStructure, ResponsibilitySetRefStructure, \
    ResponsibilitySet, VersionsRelStructure, PublicationDelivery, MultilingualString, DataObjectsRelStructure, \
    DataSourcesInFrameRelStructure, ResponsibilitySetsInFrameRelStructure, OrganisationsInFrameRelStructure, \
    OperationalContext, OperationalContextsInFrameRelStructure, VehicleTypesInFrameRelStructure, VehicleType, Block, \
    BlocksInFrameRelStructure, DayType, DayTypeAssignment, DayTypesInFrameRelStructure, \
    DayTypeAssignmentsInFrameRelStructure, AvailabilityCondition, OperatorView, VehicleJourney, \
    ValidityConditionsRelStructure, JourneysInFrameRelStructure, RoutePoint, RouteLink, Route, Line, DestinationDisplay, \
    ScheduledStopPoint, StopArea, PassengerStopAssignment, TimingPoint, TimingLink, ServiceJourneyPattern, \
    TimeDemandType, RoutePointsInFrameRelStructure, RouteLinksInFrameRelStructure, RoutesInFrameRelStructure, \
    LinesInFrameRelStructure, DestinationDisplaysInFrameRelStructure, ScheduledStopPointsInFrameRelStructure, \
    StopAreasInFrameRelStructure, StopAssignmentsInFrameRelStructure, TimingPointsInFrameRelStructure, \
    TimingLinksInFrameRelStructure, JourneyPatternsInFrameRelStructure, TimeDemandTypesInFrameRelStructure, \
    CodespacesInFrameRelStructure, CodespacesRelStructure, TransportAdministrativeZone, ZonesInFrameRelStructure, \
    NoticeAssignment, Notice, NoticesInFrameRelStructure, NoticeAssignmentsInFrameRelStructure, ServiceJourney, \
    Authority, Operator, ParticipantRef, ExternalObjectRefStructure
from refs import getId, getRef


class DutchProfile:
    codespace: Codespace
    data_source: DataSource
    version: Version

    def getResourceFrames(self, id: str = "ResourceFrame",
                         data_sources: List[DataSource]=None,
                         responsibility_sets: List[ResponsibilitySet]=None,
                         organisations: List[Union[Authority, Operator]]=None,
                         operational_contexts: List[OperationalContext]=None,
                         vehicle_types: List[VehicleType]=None,
                         zones: List[TransportAdministrativeZone]=None) -> List[ResourceFrame]:
        if data_sources is not None and len(data_sources) > 0:
            data_sources = DataSourcesInFrameRelStructure(data_source=data_sources)

        if responsibility_sets is not None and len(responsibility_sets) > 0:
            responsibility_sets = ResponsibilitySetsInFrameRelStructure(responsibility_set=responsibility_sets)

        if organisations is not None and len(organisations) > 0:
            organisations = OrganisationsInFrameRelStructure(organisation_or_transport_organisation=organisations)

        if operational_contexts is not None and len(operational_contexts) > 0:
            operational_contexts = OperationalContextsInFrameRelStructure(operational_context=operational_contexts)

        if vehicle_types is not None and len(vehicle_types) > 0:
            vehicle_types = VehicleTypesInFrameRelStructure(transport_type_dummy_type_or_train_type=vehicle_types)

        if zones is not None and len(zones) > 0:
            zones = ZonesInFrameRelStructure(choice=zones)

        if data_sources is not None or responsibility_sets is not None or organisations is not None or \
                operational_contexts is not None or vehicle_types is not None or zones is not None:
            resource_frame = ResourceFrame(
                id=getId(ResourceFrame, self.codespace, id),
                version=self.version.version,
                type_of_frame_ref=TypeOfFrameRef(ref="BISON:TypeOfFrame:NL_TT_RESOURCE", version="9.3.0"),
                data_sources=data_sources,
                responsibility_sets=responsibility_sets,
                organisations=organisations,
                operational_contexts=operational_contexts,
                vehicle_types=vehicle_types,
                zones=zones,
            )
            return [resource_frame]

        return []
    def getServiceFrames(self, id: str = "ServiceFrame",
                        route_points: List[RoutePoint] = None,
                        route_links: List[RouteLink] = None,
                        routes: List[Route] = None,
                        lines: List[Line] = None,
                        destination_displays: List[DestinationDisplay] = None,
                        scheduled_stop_points: List[ScheduledStopPoint] = None,
                        stop_areas: List[StopArea] = None,
                        stop_assignments: List[PassengerStopAssignment] = None,
                        timing_points: List[TimingPoint] = None,
                        timing_links: List[TimingLink] = None,
                        service_journey_patterns: List[ServiceJourneyPattern] = None,
                        time_demand_types: List[TimeDemandType] = None,
                        notices: List[Notice] = None,
                        notice_assignments: List[NoticeAssignment] = None,
                        ) -> List[ServiceFrame]:

        if route_points is not None and len(route_points) > 0:
            route_points = RoutePointsInFrameRelStructure(route_point=route_points)

        if route_links is not None and len(route_links) > 0:
            route_links = RouteLinksInFrameRelStructure(route_link=route_links)

        if routes is not None and len(routes) > 0:
            routes = RoutesInFrameRelStructure(route=routes)

        if lines is not None and len(lines) > 0:
            # Hoeft niet meer!
            # for line in lines:
                # if line.external_line_ref is None:
                #     line.external_line_ref = ExternalObjectRefStructure(ref="0", type_value="VetagLineNumber")
            lines = LinesInFrameRelStructure(line=lines)

        if destination_displays is not None and len(destination_displays) > 0:
            destination_displays = DestinationDisplaysInFrameRelStructure(destination_display=destination_displays)

        if scheduled_stop_points is not None and len(scheduled_stop_points) > 0:
            scheduled_stop_points = ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=scheduled_stop_points)

        if stop_areas is not None and len(stop_areas) > 0:
            stop_areas = StopAreasInFrameRelStructure(stop_area=stop_areas)

        if stop_assignments is not None and len(stop_assignments) > 0:
            stop_assignments = StopAssignmentsInFrameRelStructure(stop_assignment_or_passenger_boarding_position_assignment=stop_assignments)

        if timing_points is not None and len(timing_points) > 0:
            timing_points = TimingPointsInFrameRelStructure(timing_point=timing_points)

        if timing_links is not None and len(timing_links) > 0:
            timing_links = TimingLinksInFrameRelStructure(timing_link=timing_links)

        if service_journey_patterns is not None and len(service_journey_patterns) > 0:
            service_journey_patterns = JourneyPatternsInFrameRelStructure(journey_pattern=service_journey_patterns)

        if time_demand_types is not None and len(time_demand_types) > 0:
            time_demand_types = TimeDemandTypesInFrameRelStructure(time_demand_type=time_demand_types)

        if notices is not None and len(notices) > 0:
            notices = NoticesInFrameRelStructure(notice=notices)

        if notice_assignments is not None and len(notice_assignments) > 0:
            notice_assignments = NoticeAssignmentsInFrameRelStructure(notice_assignment=notice_assignments)

        if route_points is not None or \
            route_links is not None or \
            routes is not None or \
            lines is not None or \
            destination_displays is not None or \
            scheduled_stop_points is not None or \
            stop_areas is not None or \
            stop_assignments is not None or \
            timing_points is not None or \
            timing_links is not None or \
            service_journey_patterns is not None or \
            time_demand_types is not None or \
            notices is not None or \
            notice_assignments is not None:

            service_frame = ServiceFrame(
                id=getId(ServiceFrame, self.codespace, id),
                version=self.version.version,
                type_of_frame_ref = TypeOfFrameRef(ref="BISON:TypeOfFrame:NL_TT_SERVICE", version="9.3.0"),
                route_points=route_points,
                route_links=route_links,
                routes=routes,
                lines=lines,
                destination_displays=destination_displays,
                scheduled_stop_points=scheduled_stop_points,
                stop_areas=stop_areas,
                stop_assignments=stop_assignments,
                timing_points=timing_points,
                timing_links=timing_links,
                journey_patterns=service_journey_patterns,
                time_demand_types=time_demand_types,
                notices=notices,
                notice_assignments=notice_assignments
            )
            return [service_frame]

        return []

    def getTimetableFrame(self, id: str = "TimetableFrame",
                          content_validity_conditions: List[AvailabilityCondition] = None,
                          operator_view: OperatorView = None,
                          vehicle_journeys: List[VehicleJourney] = None,
                          ) -> List[TimetableFrame]:

        if content_validity_conditions is not None and len(content_validity_conditions) > 0:
            content_validity_conditions = ValidityConditionsRelStructure(choice=content_validity_conditions)

        if vehicle_journeys is not None and len(vehicle_journeys) > 0:
            vehicle_journeys = JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=vehicle_journeys)

        if content_validity_conditions is not None or vehicle_journeys is not None or operator_view is not None:
            timetable_frame = TimetableFrame(
                id=getId(TimetableFrame, self.codespace, id),
                version=self.version.version,
                type_of_frame_ref = TypeOfFrameRef(ref="BISON:TypeOfFrame:NL_TT_TIMETABLE", version="9.3.0"),
                content_validity_conditions=content_validity_conditions,
                operator_view=operator_view,
                vehicle_journeys=vehicle_journeys,
            )
            return [timetable_frame]

        return []

    def getServiceCalendarFrames(self, id: str = "ServiceCalendarFrame",
                                 day_types: List[DayType]=None,
                                 day_type_assignments: List[DayTypeAssignment]=None
                                 ) -> List[ServiceCalendarFrame]:
        if day_types is not None:
            day_types = DayTypesInFrameRelStructure(day_type=day_types)

        if day_type_assignments is not None:
            day_type_assignments = DayTypeAssignmentsInFrameRelStructure(day_type_assignment=day_type_assignments)

        if day_types is not None or day_type_assignments is not None:
            service_calendar_frame = ServiceCalendarFrame(
                id=getId(ServiceCalendarFrame, self.codespace, id),
                version=self.version.version,
                type_of_frame_ref=TypeOfFrameRef(ref="BISON:TypeOfFrame:NL_TT_CALENDAR", version="9.3.0"),
                day_types=day_types,
                day_type_assignments=day_type_assignments,
            )
            return [service_calendar_frame]

        return []

    def getVehicleScheduleFrames(self, id: str = "VehicleScheduleFrame",
                                 blocks: List[Block]=None) -> List[VehicleScheduleFrame]:
        if blocks is not None and len(blocks) > 0:
            blocks = BlocksInFrameRelStructure(block_or_compound_block_or_train_block=blocks)

            vehicle_schedule_frame = VehicleScheduleFrame(
                id=getId(VehicleScheduleFrame, self.codespace, id),
                version=self.version.version,
                type_of_frame_ref=TypeOfFrameRef(ref="BISON:TypeOfFrame:NL_TT_VEHICLE", version="9.3.0"),
                blocks=blocks
            )
            return [vehicle_schedule_frame]

        return []

    def getCompositeFrame(self, id: str = "CompositeFrame",
                          versions: List[Version] = None,
                          codespaces: List[Codespace] = None,
                          responsibility_set: ResponsibilitySet = None,
                          resource_frames: List[ResourceFrame] = [],
                          service_frames: List[ServiceFrame] = [],
                          timetable_frames: List[TimetableFrame] = [],
                          service_calendar_frames: List[ServiceCalendarFrame] = [],
                          vehicle_schedule_frames: List[VehicleScheduleFrame] = []):

        if versions is not None and len(versions) > 0:
            versions = VersionsRelStructure(version_ref_or_version=versions)

        if codespaces is not None and len(codespaces) > 0:
            codespaces = CodespacesRelStructure(codespace_ref_or_codespace=codespaces)

        composite_frame = CompositeFrame(
            id=getId(CompositeFrame, self.codespace, id),
            version=self.version.version,
            type_of_frame_ref=TypeOfFrameRef(ref="BISON:TypeOfFrame:NL_TT_BASELINE", version="9.3.0"),
            frame_defaults=VersionFrameDefaultsStructure(
                default_codespace_ref=getRef(self.codespace, CodespaceRefStructure),
                default_data_source_ref=getRef(self.data_source, DataSourceRefStructure),
                default_responsibility_set_ref=getRef(responsibility_set, ResponsibilitySetRefStructure),
                default_locale=LocaleStructure(time_zone="Europe/Amsterdam", default_language="nl"),
                default_location_system="EPSG:28992",
                default_system_of_units=SystemOfUnits.SI_METRES,
                default_currency="EUR",
            ),
            versions=versions,
            # codespaces=codespaces,
            frames=FramesRelStructure(common_frame=resource_frames + service_frames +
                                              timetable_frames + service_calendar_frames +
                                              vehicle_schedule_frames)
        )
        return composite_frame

    def getPublicationDelivery(self, composite_frame: CompositeFrame, description: str):
        import pytz
        tz = pytz.timezone('Europe/Amsterdam')
        publication_delivery = PublicationDelivery(
            publication_timestamp=XmlDateTime.now(tz=tz).replace(fractional_second=0),
            participant_ref=ParticipantRef(value="NDOV"),
            description=MultilingualString(value=description),
            data_objects=DataObjectsRelStructure(choice=[composite_frame]),
            version="ntx:1.1",
        )

        return publication_delivery

    def __init__(self, codespace: Codespace, data_source: DataSource, version: Version):
        self.codespace = codespace
        self.data_source = data_source
        self.version = version