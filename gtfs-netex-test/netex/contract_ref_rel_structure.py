from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .contract_ref import ContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContractRefRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "ContractRef_RelStructure"

    contract_ref: ContractRef = field(
        metadata={
            "name": "ContractRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
