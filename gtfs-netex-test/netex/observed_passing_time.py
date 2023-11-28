from dataclasses import dataclass, field
from netex.observed_passing_time_versioned_child_structure import ObservedPassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ObservedPassingTime(ObservedPassingTimeVersionedChildStructure):
    """
    OBSERVED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
