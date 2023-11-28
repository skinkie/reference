from dataclasses import dataclass, field
from typing import List, Optional, Type
from xsdata.models.datatype import XmlDateTime
from netex.alternative_texts_rel_structure import (
    AvailabilityCondition,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition,
    ValidityRuleParameter,
    ValidityTrigger,
)
from netex.closed_timestamp_range_structure import ClosedTimestampRangeStructure
from netex.composite_frame_ref import CompositeFrameRef
from netex.driver_schedule_frame_ref import DriverScheduleFrameRef
from netex.empty_type_2 import EmptyType2
from netex.fare_frame_ref import FareFrameRef
from netex.general_frame_ref import GeneralFrameRef
from netex.infrastructure_frame_ref import InfrastructureFrameRef
from netex.mobility_journey_frame_ref import MobilityJourneyFrameRef
from netex.mobility_service_frame_ref import MobilityServiceFrameRef
from netex.network_filter_by_value_structure import NetworkFilterByValueStructure
from netex.resource_frame_ref import ResourceFrameRef
from netex.sales_transaction_frame_ref import SalesTransactionFrameRef
from netex.service_calendar_frame_ref import ServiceCalendarFrameRef
from netex.service_frame_ref import ServiceFrameRef
from netex.site_frame_ref import SiteFrameRef
from netex.timetable_frame_ref import TimetableFrameRef
from netex.topic_structure import TopicStructure
from netex.type_of_frame_ref import TypeOfFrameRef
from netex.vehicle_schedule_frame_ref import VehicleScheduleFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkFrameTopicStructure(TopicStructure):
    """
    Type for a Data Object Filter Topic.
    """
    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Current",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChangedSince",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CurrentAt",
                    "type": XmlDateTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HistoricBetween",
                    "type": ClosedTimestampRangeStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "selectionValidityConditions",
                    "type": Type["NetworkFrameTopicStructure.SelectionValidityConditions"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice_1: List[object] = field(
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
                {
                    "name": "NetworkFilterByValue",
                    "type": NetworkFilterByValueStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )

    @dataclass(unsafe_hash=True, kw_only=True)
    class SelectionValidityConditions:
        choice: List[object] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "SimpleAvailabilityCondition",
                        "type": SimpleAvailabilityCondition,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidDuring",
                        "type": ValidDuring,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "AvailabilityCondition",
                        "type": AvailabilityCondition,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidityRuleParameter",
                        "type": ValidityRuleParameter,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidityTrigger",
                        "type": ValidityTrigger,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidityCondition",
                        "type": ValidityCondition,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            }
        )
