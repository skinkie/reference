from dataclasses import dataclass, field
from netex.parking_bay_version_structure import ParkingBayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBay(ParkingBayVersionStructure):
    """
    An individual place to park a VEHICLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
