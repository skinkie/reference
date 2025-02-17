from dataclasses import dataclass

from .parking_properties_versioned_child_structure import ParkingPropertiesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingProperties(ParkingPropertiesVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
