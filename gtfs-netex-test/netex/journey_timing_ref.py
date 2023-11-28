from dataclasses import dataclass
from netex.journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyTimingRef(JourneyTimingRefStructure):
    """
    Reference to a JOURNEY TIMING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
