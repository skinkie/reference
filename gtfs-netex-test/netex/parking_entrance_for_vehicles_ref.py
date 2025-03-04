from dataclasses import dataclass

from .parking_entrance_for_vehicles_ref_structure import ParkingEntranceForVehiclesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingEntranceForVehiclesRef(ParkingEntranceForVehiclesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
