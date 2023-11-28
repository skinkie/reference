from dataclasses import dataclass
from netex.journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternHeadwayRefStructure(JourneyTimingRefStructure):
    """
    Type for a reference to a JOURNEY PATTERN HEADWAY.
    """
