from dataclasses import dataclass, field

from .fare_contract_ref import FareContractRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ContractRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "contractRefs_RelStructure"

    fare_contract_ref: list[FareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "FareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
