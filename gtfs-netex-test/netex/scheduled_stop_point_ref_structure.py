from dataclasses import dataclass

from .timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ScheduledStopPointRefStructure(TimingPointRefStructure):
    pass
