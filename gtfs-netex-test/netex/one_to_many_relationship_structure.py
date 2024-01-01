from dataclasses import dataclass, field
from .modification_set_enumeration import ModificationSetEnumeration
from .relationship_structure import RelationshipStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OneToManyRelationshipStructure(RelationshipStructure):
    class Meta:
        name = "oneToManyRelationshipStructure"

    modification_set: ModificationSetEnumeration = field(
        default=ModificationSetEnumeration.ALL,
        metadata={
            "name": "modificationSet",
            "type": "Attribute",
        },
    )
