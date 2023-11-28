from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_machine_readability_ref import TypeOfMachineReadabilityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMachineReadabilityRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF MACHINE READABILITY.
    """
    class Meta:
        name = "TypeOfMachineReadabilityRefs_RelStructure"

    type_of_machine_readability_ref: List[TypeOfMachineReadabilityRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfMachineReadabilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
