from dataclasses import dataclass

from .fare_contract_entry_ref_structure import FareContractEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesTransactionRefStructure(FareContractEntryRefStructure):
    pass
