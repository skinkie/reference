from dataclasses import dataclass

from .vehicle_pooling_driver_info_ref_structure import VehiclePoolingDriverInfoRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingDriverInfoRef(VehiclePoolingDriverInfoRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
