from dataclasses import dataclass, field
from netex.parking_properties_versioned_child_structure import ParkingPropertiesVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingProperties(ParkingPropertiesVersionedChildStructure):
    """
    Properties of a PARKING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
