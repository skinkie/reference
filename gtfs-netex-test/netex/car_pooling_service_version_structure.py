from dataclasses import dataclass
from netex.vehicle_pooling_service_version_structure import VehiclePoolingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarPoolingServiceVersionStructure(VehiclePoolingServiceVersionStructure):
    """
    Type for CAR POOLING SERVICE.
    """
    class Meta:
        name = "CarPoolingService_VersionStructure"
