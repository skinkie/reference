from dataclasses import dataclass, field
from typing import Optional

from .abstract_capabilities_structure import AbstractCapabilitiesStructure
from .capability_access_control_structure import CapabilityAccessControlStructure
from .check_line_ref import CheckLineRef
from .check_monitoring_ref import CheckMonitoringRef
from .check_operator_ref import CheckOperatorRef
from .extensions_1 import Extensions1
from .filter_by_direction_ref import FilterByDirectionRef
from .filter_by_line_ref import FilterByLineRef
from .filter_by_monitoring_ref import FilterByMonitoringRef
from .stop_timetable_capability_request_policy_structure import StopTimetableCapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableServiceCapabilitiesStructure(AbstractCapabilitiesStructure):
    topic_filtering: Optional["StopTimetableServiceCapabilitiesStructure.TopicFiltering"] = field(
        default=None,
        metadata={
            "name": "TopicFiltering",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_policy: Optional[StopTimetableCapabilityRequestPolicyStructure] = field(
        default=None,
        metadata={
            "name": "RequestPolicy",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_control: Optional["StopTimetableServiceCapabilitiesStructure.AccessControl"] = field(
        default=None,
        metadata={
            "name": "AccessControl",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class TopicFiltering:
        filter_by_monitoring_ref: FilterByMonitoringRef = field(
            metadata={
                "name": "FilterByMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        filter_by_line_ref: FilterByLineRef = field(
            metadata={
                "name": "FilterByLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            }
        )
        filter_by_direction_ref: Optional[FilterByDirectionRef] = field(
            default=None,
            metadata={
                "name": "FilterByDirectionRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )

    @dataclass(kw_only=True)
    class AccessControl(CapabilityAccessControlStructure):
        check_operator_ref: Optional[CheckOperatorRef] = field(
            default=None,
            metadata={
                "name": "CheckOperatorRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        check_line_ref: Optional[CheckLineRef] = field(
            default=None,
            metadata={
                "name": "CheckLineRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
        check_monitoring_ref: Optional[CheckMonitoringRef] = field(
            default=None,
            metadata={
                "name": "CheckMonitoringRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
            },
        )
