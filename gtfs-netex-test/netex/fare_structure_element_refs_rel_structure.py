from dataclasses import dataclass, field

from .fare_structure_element_ref import FareStructureElementRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareStructureElementRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "fareStructureElementRefs_RelStructure"

    fare_structure_element_ref: list[FareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
