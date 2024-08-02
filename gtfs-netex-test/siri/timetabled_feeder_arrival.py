from dataclasses import dataclass

from .timetabled_feeder_arrival_structure import TimetabledFeederArrivalStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetabledFeederArrival(TimetabledFeederArrivalStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
