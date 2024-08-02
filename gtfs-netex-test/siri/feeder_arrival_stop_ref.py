from dataclasses import dataclass

from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FeederArrivalStopRef(StopPointRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
