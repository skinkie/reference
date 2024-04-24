from dataclasses import dataclass

from .contract_ref_structure import ContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplyContractRefStructure(ContractRefStructure):
    pass
