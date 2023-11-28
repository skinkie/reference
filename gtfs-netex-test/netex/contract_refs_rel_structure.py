from dataclasses import dataclass, field
from typing import List
from netex.fare_contract_ref import FareContractRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ContractRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to FARE CONTRACT.
    """
    class Meta:
        name = "contractRefs_RelStructure"

    fare_contract_ref: List[FareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
