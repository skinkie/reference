from dataclasses import dataclass

from .monitored_feeder_arrival_structure import MonitoredFeederArrivalStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredFeederArrival(MonitoredFeederArrivalStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
