from dataclasses import dataclass
from .alternative_texts_rel_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataManagedObjectViewStructure(DataManagedObjectStructure):
    class Meta:
        name = "DataManagedObject_ViewStructure"
