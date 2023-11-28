from dataclasses import dataclass, field
from netex.parking_component_version_structure import ParkingComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingComponent(ParkingComponentVersionStructure):
    """
    Component within a PARKING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
