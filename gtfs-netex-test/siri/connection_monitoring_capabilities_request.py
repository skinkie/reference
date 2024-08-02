from dataclasses import dataclass

from .service_capabilities_request_structure import ServiceCapabilitiesRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
