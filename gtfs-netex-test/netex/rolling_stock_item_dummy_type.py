from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RollingStockItemDummyType(DataManagedObjectStructure):
    class Meta:
        name = "RollingStockItem_DummyType"
        namespace = "http://www.netex.org.uk/netex"
