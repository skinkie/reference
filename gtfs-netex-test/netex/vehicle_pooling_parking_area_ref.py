from dataclasses import dataclass
from netex.vehicle_pooling_parking_area_ref_structure import VehiclePoolingParkingAreaRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingParkingAreaRef(VehiclePoolingParkingAreaRefStructure):
    """Reference to a VEHICLE POOLING PARKING AREA.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
