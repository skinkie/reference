from dataclasses import dataclass, field
from netex.alternative_name_versioned_child_structure import AlternativeNameVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeName(AlternativeNameVersionedChildStructure):
    """
    Alternative Name.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
