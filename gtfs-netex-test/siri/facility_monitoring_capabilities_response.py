from dataclasses import dataclass

from .facility_monitoring_capabilities_response_structure import FacilityMonitoringCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringCapabilitiesResponse(FacilityMonitoringCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
