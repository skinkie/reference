from dataclasses import dataclass, field
from netex.suitability_versioned_child_structure import SuitabilityVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class Suitability(SuitabilityVersionedChildStructure):
    """
    The SUITABILTY of a component to meet a specific USER NEED.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
