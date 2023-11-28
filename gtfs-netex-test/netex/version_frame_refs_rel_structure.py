from dataclasses import dataclass, field
from typing import List
from netex.composite_frame_ref import CompositeFrameRef
from netex.driver_schedule_frame_ref import DriverScheduleFrameRef
from netex.fare_frame_ref import FareFrameRef
from netex.general_frame_ref import GeneralFrameRef
from netex.infrastructure_frame_ref import InfrastructureFrameRef
from netex.mobility_journey_frame_ref import MobilityJourneyFrameRef
from netex.mobility_service_frame_ref import MobilityServiceFrameRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.resource_frame_ref import ResourceFrameRef
from netex.sales_transaction_frame_ref import SalesTransactionFrameRef
from netex.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.service_frame_ref import ServiceFrameRef
from netex.site_frame_ref import SiteFrameRef
from netex.timetable_frame_ref import TimetableFrameRef
from netex.vehicle_schedule_frame_ref import VehicleScheduleFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VersionFrameRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a VERSION FRAME.
    """
    class Meta:
        name = "versionFrameRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobilityJourneyFrameRef",
                    "type": MobilityJourneyFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobilityServiceFrameRef",
                    "type": MobilityServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrameRef",
                    "type": SalesTransactionFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrameRef",
                    "type": FareFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrameRef",
                    "type": ServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrameRef",
                    "type": DriverScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrameRef",
                    "type": VehicleScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrameRef",
                    "type": TimetableFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrameRef",
                    "type": SiteFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrameRef",
                    "type": InfrastructureFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrameRef",
                    "type": GeneralFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrameRef",
                    "type": ResourceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrameRef",
                    "type": ServiceCalendarFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrameRef",
                    "type": CompositeFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
