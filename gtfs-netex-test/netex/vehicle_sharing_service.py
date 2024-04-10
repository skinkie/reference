from dataclasses import dataclass

from .vehicle_sharing_service_version_structure import VehicleSharingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingService(VehicleSharingServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
