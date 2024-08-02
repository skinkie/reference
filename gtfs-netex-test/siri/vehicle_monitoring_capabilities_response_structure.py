from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .vehicle_monitoring_permissions import VehicleMonitoringPermissions
from .vehicle_monitoring_service_capabilities import VehicleMonitoringServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    vehicle_monitoring_service_capabilities: Optional[VehicleMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_monitoring_permissions: Optional[VehicleMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringPermissions",
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
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
