from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_contract import FareContract
from netex.fare_contract_ref import FareContractRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE CONTRACTs.
    """
    class Meta:
        name = "fareContracts_RelStructure"

    fare_contract_ref_or_fare_contract: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareContractRef",
                    "type": FareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareContract",
                    "type": FareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
