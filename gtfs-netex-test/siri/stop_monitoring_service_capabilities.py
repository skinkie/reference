from dataclasses import dataclass

from .stop_monitoring_service_capabilities_structure import StopMonitoringServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringServiceCapabilities(StopMonitoringServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
