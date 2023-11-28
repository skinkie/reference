from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_fare_contract_ref import TypeOfFareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareContractRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPEs OF FARE CONTRACT.
    """
    class Meta:
        name = "typeOfFareContractRefs_RelStructure"

    type_of_fare_contract_ref: List[TypeOfFareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
