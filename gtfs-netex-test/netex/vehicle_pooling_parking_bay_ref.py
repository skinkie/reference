from dataclasses import dataclass
from netex.vehicle_pooling_parking_bay_ref_structure import VehiclePoolingParkingBayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingParkingBayRef(VehiclePoolingParkingBayRefStructure):
    """Reference to a VEHICLE POOLING PARKING BAY.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
