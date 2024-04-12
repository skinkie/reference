import datetime
from typing import List

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.models.datatype import XmlDateTime

from netex import PublicationDelivery, DataObjectsRelStructure, CompositeFrame, CodespacesRelStructure, \
    VersionsRelStructure, FramesRelStructure, Codespace, ServiceFrame, TypeOfFrame, TypeOfFrameRef, ResourceFrame, \
    DataSourcesInFrameRelStructure, OrganisationsInFrameRelStructure, OperationalContextsInFrameRelStructure, \
    TimetableFrame, LinesInFrameRelStructure, ScheduledStopPointsInFrameRelStructure, JourneysInFrameRelStructure, \
    JourneyPatternsInFrameRelStructure, RoutesInFrameRelStructure, RoutePointsInFrameRelStructure, \
    RouteLinksInFrameRelStructure, DataManagedObjectStructure, Line, TransportOrganisationRefsRelStructure, ServiceLink
from refs import getId
# from src.refs import setIdVersion
from timetabledpassingtimesprofile import TimetablePassingTimesProfile


class EPIPNeTexProfile(TimetablePassingTimesProfile):
    codespace: Codespace

    @staticmethod
    def clean_element(element: DataManagedObjectStructure):
        element.derived_from_object_ref = None
        element.version = None
        element.data_source_ref_attribute = None

    # def getServiceLinks(self) -> List[ServiceLink]:
    #     for x in self.timing_links:


    def getResourceFrame(self) -> ResourceFrame:
        resource_frame = ResourceFrame(id=getId(ResourceFrame, self.codespace, "ResourceFrame"), version=self.version.version)
        # resource_frame.data_sources = DataSourcesInFrameRelStructure(data_source=[self.data_source])
        # TODO: Zone information can be obtained from stops.txt
        # resource_frame.zones = ZonesInFrameRelStructure(transport_administrative_zone=[transport_administrative_zone])
        # resource_frame.organisations = OrganisationsInFrameRelStructure(operator=self.operators)
        # resource_frame.operational_contexts = OperationalContextsInFrameRelStructure(
        #     operational_context=self.getOperationalContexts())
        # resource_frame.vehicle_types = VehicleTypesInFrameRelStructure(compound_train_or_train_or_vehicle_type=getVehicleTypes(codespace))
        # resource_frame.vehicles = VehiclesInFrameRelStructure(train_element_or_vehicle=getVehicles(codespace))
        return resource_frame

    def getTimetableFrame(self, clean=False) -> TimetableFrame:
        self.getTimetabledPassingTimes(force=False, clean=clean)

        if clean:
            for element in self.service_journeys:
                EPIPNeTexProfile.clean_element(element)

        timetable_frame = TimetableFrame(id = "TimetableFrame")
        timetable_frame.vehicle_journeys = JourneysInFrameRelStructure(vehicle_journey_or_dated_vehicle_journey_or_normal_dated_vehicle_journey_or_service_journey_or_dated_service_journey_or_dead_run_or_special_service_or_template_service_journey=self.service_journeys)
        return timetable_frame

    @staticmethod
    def clean_line(line: Line):
        if line.operator_ref and line.authority_ref:
            line.additional_operators = TransportOrganisationRefsRelStructure(transport_organisation_ref=[line.operator_ref])
            line.operator_ref = None

    def getServiceFrame(self, clean=False) -> ServiceFrame:
        if clean:
            for element in self.lines:
                EPIPNeTexProfile.clean_line(element)
                EPIPNeTexProfile.clean_element(element)
            for element in self.flexible_lines:
                EPIPNeTexProfile.clean_element(element)
            for element in self.scheduled_stop_points:
                EPIPNeTexProfile.clean_element(element)
            for element in self.service_journey_patterns:
                element.route_view = None
                element.direction_type = None
                EPIPNeTexProfile.clean_element(element)
                for stop_point_in_journey_pattern in element.points_in_sequence.point_in_journey_pattern_or_stop_point_in_journey_pattern_or_timing_point_in_journey_pattern:
                    EPIPNeTexProfile.clean_element(stop_point_in_journey_pattern)
            for element in self.routes:
                EPIPNeTexProfile.clean_element(element)
                for route_point in element.points_in_sequence.point_on_route:
                    EPIPNeTexProfile.clean_element(route_point)
            for element in self.route_points:
                EPIPNeTexProfile.clean_element(element)
            for element in self.route_links:
                EPIPNeTexProfile.clean_element(element)

        service_frame = ServiceFrame(id = "ServiceFrame")
        service_frame.type_of_frame_ref = TypeOfFrameRef(ref="EPIP:EU_PI_NETWORK")
        service_frame.lines = LinesInFrameRelStructure(line=(self.lines + self.flexible_lines))

        # TODO service_frame.destination_displays

        service_frame.scheduled_stop_points = ScheduledStopPointsInFrameRelStructure(scheduled_stop_point=self.scheduled_stop_points)

        # TODO service_frame.service_links =
        # TODO service_frame.connections =
        # TODO service_frame.stop_assignments =

        service_frame.journey_patterns = JourneyPatternsInFrameRelStructure(journey_pattern=self.service_journey_patterns)

        # Leesbaarheid
        # service_frame.routes = RoutesInFrameRelStructure(route=self.routes)
        # service_frame.route_points = RoutePointsInFrameRelStructure(route_point=self.route_points)
        # if len(self.route_links) > 0:
        #     service_frame.route_links = RouteLinksInFrameRelStructure(route_links=self.route_links)

        return service_frame

    def getCompositeFrame(self) -> CompositeFrame:
        composite_frame = CompositeFrame(id=getId(CompositeFrame, self.codespace, self.data_source.short_name.value), version=self.version.version)
        composite_frame.type_of_frame_ref = TypeOfFrameRef(ref="EPIP:EU_PI_NETWORK_OFFER")
        composite_frame.frame_defaults = self.frame_defaults
        composite_frame.codespaces = CodespacesRelStructure(codespace_ref_or_codespace=[self.codespace])
        composite_frame.versions = None

        # ServiceJourneyPatterns may be computed here:
        timetable_frame = self.getTimetableFrame(clean=True)
        service_frame = self.getServiceFrame(clean=True)

        composite_frame.frames = FramesRelStructure(common_frame=[self.getResourceFrame()] + [service_frame] + [timetable_frame])

        return composite_frame

    def getPublicationDelivery(self) -> PublicationDelivery:
        composite_frame = self.getCompositeFrame()

        publication_delivery = PublicationDelivery(
            publication_timestamp=XmlDateTime.from_datetime(datetime.datetime.now()))
        publication_delivery.version = "ntx:1.1"
        publication_delivery.participant_ref = "NDOV"
        publication_delivery.description = "NeTEx export"
        publication_delivery.data_objects = DataObjectsRelStructure(choice=[composite_frame])

        return publication_delivery

    def __init__(self):
        pass
        # self.codespace, self.data_source, self.version, self.frame_defaults = self.getCodespaceAndDataSource()
        # self.operators = self.getOperators()
        # self.lines = self.getLines()
        # self.routes, self.route_points, self.route_links = self.getRoutes()
        # self.stop_areas = self.getStopAreas()
        # self.scheduled_stop_points = self.getScheduledStopPoints()
        # self.availability_conditions = self.getAvailabilityConditions()
        # self.service_journeys = self.getServiceJourneys()
        # self.service_journey_patterns, self.timing_links = self.getServiceJourneyPatterns()
        # self.time_demand_types = self.getTimeDemandTypes()

