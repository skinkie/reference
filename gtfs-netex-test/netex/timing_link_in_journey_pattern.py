from dataclasses import dataclass, field
from netex.timing_link_in_journey_pattern_versioned_child_structure import TimingLinkInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingLinkInJourneyPattern(TimingLinkInJourneyPatternVersionedChildStructure):
    """The position of a TIMING LINK in a JOURNEY PATTERN.

    This ENTITY is needed if a TIMING LINK is repeated in the same
    JOURNEY PATTERN, and separate information is to be stored about each
    iteration of the TIMING LINK.

    :ivar id:
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
