from dataclasses import dataclass, field
from netex.service_link_in_journey_pattern_versioned_child_structure import ServiceLinkInJourneyPatternVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkInJourneyPattern(ServiceLinkInJourneyPatternVersionedChildStructure):
    """The use of a SERVICE LINK in a specified order.

    within a JOURNEY PATTERN or SERVICE PATTERN.

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
