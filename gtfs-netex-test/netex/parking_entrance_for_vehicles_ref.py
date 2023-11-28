from dataclasses import dataclass
from netex.parking_entrance_for_vehicles_ref_structure import ParkingEntranceForVehiclesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingEntranceForVehiclesRef(ParkingEntranceForVehiclesRefStructure):
    """
    Reference to a PARKING VEHICLE ENTRANCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
