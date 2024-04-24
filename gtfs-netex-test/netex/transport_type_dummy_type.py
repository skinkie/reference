from dataclasses import dataclass

from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportTypeDummyType(DataManagedObjectStructure):
    class Meta:
        name = "TransportType_DummyType"
        namespace = "http://www.netex.org.uk/netex"
