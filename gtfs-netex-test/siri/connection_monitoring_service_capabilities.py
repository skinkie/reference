from dataclasses import dataclass

from .connection_monitoring_service_capabilities_structure import ConnectionMonitoringServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringServiceCapabilities(ConnectionMonitoringServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
