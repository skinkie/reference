from dataclasses import dataclass
from netex.relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StrictContainmentAggregationStructure(RelationshipStructure):
    """Type for an Implementation of a strict aggregate  relationship by value,
    where the contained element is a child of the parent.

    A one to many relationship from the source, the containing parent,
    to the child instance.
    """
    class Meta:
        name = "strictContainmentAggregationStructure"
