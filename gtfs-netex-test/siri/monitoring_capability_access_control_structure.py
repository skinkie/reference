from dataclasses import dataclass, field
from typing import Optional

from .capability_access_control_structure import CapabilityAccessControlStructure
from .check_line_ref import CheckLineRef
from .check_monitoring_ref import CheckMonitoringRef
from .check_operator_ref import CheckOperatorRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoringCapabilityAccessControlStructure(CapabilityAccessControlStructure):
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
