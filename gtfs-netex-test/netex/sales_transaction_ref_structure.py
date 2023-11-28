from dataclasses import dataclass
from netex.fare_contract_entry_ref_structure import FareContractEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesTransactionRefStructure(FareContractEntryRefStructure):
    """
    Type for Reference to a SALES TRANSACTION.
    """
