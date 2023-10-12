from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RelationshipStructure:
    """
    Abstract Type for a serialisation of a NeTEx relationship.

    :ivar id: Identifier of the relationship.
    """
    class Meta:
        name = "relationshipStructure"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
