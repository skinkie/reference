from dataclasses import dataclass
from netex.fare_contract_ref_structure import FareContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractRef(FareContractRefStructure):
    """
    Reference to a FARE CONTRACT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
