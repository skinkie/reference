from dataclasses import dataclass, field
from netex.link_in_journey_pattern_versioned_child_structure import LinkInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkInJourneyPattern(LinkInJourneyPatternVersionedChildStructure):
    """
    A SERVICE LINK or TIMING LINK in a JOURNEY PATTERN with its order in that
    JOURNEY PATTERN.

    :ivar id: Identifier of ENTITY.
    :ivar order: Order of LINK in sequence.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
