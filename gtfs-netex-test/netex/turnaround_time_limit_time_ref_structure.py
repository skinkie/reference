from dataclasses import dataclass

from .journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TurnaroundTimeLimitTimeRefStructure(JourneyTimingRefStructure):
    pass
