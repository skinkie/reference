from dataclasses import dataclass

from .journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternLayoverRefStructure(JourneyTimingRefStructure):
    pass
