from dataclasses import dataclass
from netex.supply_contract_ref_structure import SupplyContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SupplyContractRef(SupplyContractRefStructure):
    """
    Reference to a SUPPLY CONTRACT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
