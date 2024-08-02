from dataclasses import dataclass

from .monitored_stop_visit_structure import MonitoredStopVisitStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredStopVisit(MonitoredStopVisitStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
