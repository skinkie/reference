from dataclasses import dataclass

from .monitored_feeder_arrival_cancellation_structure import MonitoredFeederArrivalCancellationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredFeederArrivalCancellation(MonitoredFeederArrivalCancellationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
