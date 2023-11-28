from dataclasses import dataclass
from netex.vehicle_pooling_driver_info_ref_structure import VehiclePoolingDriverInfoRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingDriverInfoRef(VehiclePoolingDriverInfoRefStructure):
    """Reference to a VEHICLE POOLING DRIVER INFO.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
