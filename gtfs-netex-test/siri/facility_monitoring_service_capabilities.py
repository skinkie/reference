from dataclasses import dataclass

from .facility_monitoring_service_capabilities_structure import FacilityMonitoringServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringServiceCapabilities(FacilityMonitoringServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
