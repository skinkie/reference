from dataclasses import dataclass

from .timetabled_feeder_arrival_cancellation_structure import TimetabledFeederArrivalCancellationStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetabledFeederArrivalCancellation(TimetabledFeederArrivalCancellationStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
