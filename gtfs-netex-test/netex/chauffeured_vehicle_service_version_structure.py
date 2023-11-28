from dataclasses import dataclass
from netex.vehicle_pooling_service_version_structure import VehiclePoolingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChauffeuredVehicleServiceVersionStructure(VehiclePoolingServiceVersionStructure):
    """
    Type for ChauffeuredVehicle SERVICE.
    """
    class Meta:
        name = "ChauffeuredVehicleService_VersionStructure"
