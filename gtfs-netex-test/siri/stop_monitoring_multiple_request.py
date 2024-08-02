from dataclasses import dataclass

from .stop_monitoring_multiple_request_structure import StopMonitoringMultipleRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopMonitoringMultipleRequest(StopMonitoringMultipleRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
