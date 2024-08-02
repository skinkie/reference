from dataclasses import dataclass, field

from .abstract_topic_permission_structure import AbstractTopicPermissionStructure
from .monitoring_ref_structure import MonitoringRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitorPermissionStructure(AbstractTopicPermissionStructure):
    monitoring_ref: MonitoringRefStructure = field(
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
