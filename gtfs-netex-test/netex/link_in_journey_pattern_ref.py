from dataclasses import dataclass
from netex.link_in_journey_pattern_ref_structure import LinkInJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkInJourneyPatternRef(LinkInJourneyPatternRefStructure):
    """Reference to a LINK IN JOURNEY PATTERN.

    If Given by Context does not need to stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
