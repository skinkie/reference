from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_proof_ref import TypeOfProofRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypesOfProofRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYOP OF PRROF .
    """
    class Meta:
        name = "typesOfProofRefs_RelStructure"

    type_of_proof_ref: List[TypeOfProofRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfProofRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
