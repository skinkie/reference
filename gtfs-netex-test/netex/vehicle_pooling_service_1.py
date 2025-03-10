from dataclasses import dataclass

from .vehicle_pooling_service_version_structure import VehiclePoolingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingService1(VehiclePoolingServiceVersionStructure):
    class Meta:
        name = "VehiclePoolingService"
        namespace = "http://www.netex.org.uk/netex"
