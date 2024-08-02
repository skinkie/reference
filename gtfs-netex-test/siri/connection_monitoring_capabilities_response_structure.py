from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .connection_monitoring_permissions import ConnectionMonitoringPermissions
from .connection_monitoring_service_capabilities import ConnectionMonitoringServiceCapabilities
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    connection_monitoring_service_capabilities: Optional[ConnectionMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_permissions: Optional[ConnectionMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringPermissions",
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
