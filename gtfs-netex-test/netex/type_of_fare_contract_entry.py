from dataclasses import dataclass

from .type_of_fare_contract_entry_version_structure import TypeOfFareContractEntryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfFareContractEntry(TypeOfFareContractEntryVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
