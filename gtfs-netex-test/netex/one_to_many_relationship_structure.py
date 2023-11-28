from dataclasses import dataclass, field
from netex.modification_set_enumeration import ModificationSetEnumeration
from netex.relationship_structure import RelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OneToManyRelationshipStructure(RelationshipStructure):
    """Type for an Implementation of a one to many relationship .

    A one to many relationship from the source (one) to the target
    (many)

    :ivar modification_set: Whether this is a list of all (revise) or
        just changes.
    """
    class Meta:
        name = "oneToManyRelationshipStructure"

    modification_set: ModificationSetEnumeration = field(
        default=ModificationSetEnumeration.ALL,
        metadata={
            "name": "modificationSet",
            "type": "Attribute",
        }
    )
