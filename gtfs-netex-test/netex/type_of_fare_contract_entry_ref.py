from dataclasses import dataclass
from netex.type_of_fare_contract_entry_ref_structure import TypeOfFareContractEntryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareContractEntryRef(TypeOfFareContractEntryRefStructure):
    """
    Reference to a TYPE OF FARE CONTRACT ENTRY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
