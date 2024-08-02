from dataclasses import dataclass

from .connection_monitoring_request_structure import ConnectionMonitoringRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringRequest(ConnectionMonitoringRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
