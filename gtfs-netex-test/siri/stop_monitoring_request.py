from dataclasses import dataclass

from .stop_monitoring_request_structure import StopMonitoringRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringRequest(StopMonitoringRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
