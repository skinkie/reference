from dataclasses import dataclass, field
from typing import List
from netex.fare_structure_element_ref import FareStructureElementRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareStructureElementRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a  FARE STRUCTURE ELEMENT.
    """
    class Meta:
        name = "fareStructureElementRefs_RelStructure"

    fare_structure_element_ref: List[FareStructureElementRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
