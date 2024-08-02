from dataclasses import dataclass

from .stop_monitoring_capabilities_response_structure import StopMonitoringCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringCapabilitiesResponse(StopMonitoringCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
