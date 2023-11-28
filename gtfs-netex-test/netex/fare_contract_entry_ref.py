from dataclasses import dataclass
from netex.fare_contract_entry_ref_structure import FareContractEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractEntryRef(FareContractEntryRefStructure):
    """
    Reference to a FARE CONTRACT ENTRY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
