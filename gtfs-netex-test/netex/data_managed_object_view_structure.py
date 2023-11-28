from dataclasses import dataclass
from netex.alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataManagedObjectViewStructure(DataManagedObjectStructure):
    """
    Type for MANAGED OBJECT VIEW.
    """
    class Meta:
        name = "DataManagedObject_ViewStructure"
