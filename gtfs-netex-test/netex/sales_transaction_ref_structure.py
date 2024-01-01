from dataclasses import dataclass
from .fare_contract_entry_ref_structure import FareContractEntryRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesTransactionRefStructure(FareContractEntryRefStructure):
    value: RestrictedVar
