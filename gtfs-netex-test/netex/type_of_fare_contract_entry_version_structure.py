from dataclasses import dataclass
from netex.type_of_entity_version_structure import TypeOfEntityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareContractEntryVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF FARE CONTRACT ENTRY.
    """
    class Meta:
        name = "TypeOfFareContractEntry_VersionStructure"
