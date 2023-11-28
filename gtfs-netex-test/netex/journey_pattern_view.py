from dataclasses import dataclass
from netex.journey_pattern_derived_view_structure import JourneyPatternDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPatternView(JourneyPatternDerivedViewStructure):
    """
    Simplified view of a JOURNEY PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
