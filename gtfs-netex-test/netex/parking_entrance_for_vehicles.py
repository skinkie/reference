from dataclasses import dataclass, field
from netex.parking_entrance_for_vehicles_version_structure import ParkingEntranceForVehiclesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingEntranceForVehicles(ParkingEntranceForVehiclesVersionStructure):
    """
    Designated Place within a PARKING for a VEHICLE to enter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
