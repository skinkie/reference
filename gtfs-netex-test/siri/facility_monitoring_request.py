from dataclasses import dataclass

from .facility_monitoring_request_structure import FacilityMonitoringRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringRequest(FacilityMonitoringRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
