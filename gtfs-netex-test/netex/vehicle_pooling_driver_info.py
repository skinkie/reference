from dataclasses import dataclass

from .vehicle_pooling_driver_info_version_structure import VehiclePoolingDriverInfoVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingDriverInfo(VehiclePoolingDriverInfoVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
