from dataclasses import dataclass
from netex.journey_pattern_layover_ref_structure import JourneyPatternLayoverRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternLayoverRef(JourneyPatternLayoverRefStructure):
    """
    Reference to a JOURNEY PATTERN LAYOVER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
