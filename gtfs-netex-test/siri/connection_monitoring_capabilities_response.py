from dataclasses import dataclass

from .connection_monitoring_capabilities_response_structure import ConnectionMonitoringCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringCapabilitiesResponse(ConnectionMonitoringCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
