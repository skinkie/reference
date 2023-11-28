from dataclasses import dataclass
from netex.alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareContractEntry(DataManagedObjectStructure):
    """
    Dummy type for FARE CONTRACT ENTRY.
    """
    class Meta:
        name = "FareContractEntry_"
        namespace = "http://www.netex.org.uk/netex"
