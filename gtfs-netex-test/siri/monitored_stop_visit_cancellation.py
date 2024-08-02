from dataclasses import dataclass

from .monitored_stop_visit_cancellation_structure import MonitoredStopVisitCancellationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredStopVisitCancellation(MonitoredStopVisitCancellationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
