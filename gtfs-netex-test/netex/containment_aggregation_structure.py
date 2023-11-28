from dataclasses import dataclass, field
from netex.modification_set_enumeration import ModificationSetEnumeration
from netex.relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContainmentAggregationStructure(RelationshipStructure):
    """
    Type for an Implementation of an aggregate  relationship by reference or value,
    where the contained element or reference  is included in the XML as  a child of
    the parent.

    :ivar modification_set: Whether this is a list of all (revise) or
        just changes.
    """
    class Meta:
        name = "containmentAggregationStructure"

    modification_set: ModificationSetEnumeration = field(
        default=ModificationSetEnumeration.ALL,
        metadata={
            "name": "modificationSet",
            "type": "Attribute",
        }
    )
