from dataclasses import dataclass, field

from .abstract_topic_permission_structure import AbstractTopicPermissionStructure
from .vehicle_monitoring_ref_structure import VehicleMonitoringRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitorPermissionStructure(AbstractTopicPermissionStructure):
    vehicle_monitoring_ref: VehicleMonitoringRefStructure = field(
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
