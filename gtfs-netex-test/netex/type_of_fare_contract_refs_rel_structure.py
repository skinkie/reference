from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .type_of_fare_contract_ref import TypeOfFareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfFareContractRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "typeOfFareContractRefs_RelStructure"

    type_of_fare_contract_ref: list[TypeOfFareContractRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfFareContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
