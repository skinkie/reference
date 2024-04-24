from dataclasses import dataclass, field
from typing import Optional, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .contract import Contract
from .contract_ref import ContractRef
from .supply_contract_ref import SupplyContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContractRefRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "ContractRef_RelStructure"

    supply_contract_ref_or_contract_ref_or_contract: Optional[Union[SupplyContractRef, ContractRef, Contract]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplyContractRef",
                    "type": SupplyContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ContractRef",
                    "type": ContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Contract",
                    "type": Contract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
