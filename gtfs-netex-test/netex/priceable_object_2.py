from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceableObject2(DataManagedObjectStructure):
    class Meta:
        name = "PriceableObject_"
        namespace = "http://www.netex.org.uk/netex"
