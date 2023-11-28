from dataclasses import dataclass, field
from netex.type_of_fare_contract_entry_version_structure import TypeOfFareContractEntryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareContractEntry(TypeOfFareContractEntryVersionStructure):
    """
    A classification of a FARE CONTRACT ENTRY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
