from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .stop_monitoring_permissions import StopMonitoringPermissions
from .stop_monitoring_service_capabilities import StopMonitoringServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    stop_monitoring_service_capabilities: Optional[StopMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "StopMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_monitoring_permissions: Optional[StopMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "StopMonitoringPermissions",
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
