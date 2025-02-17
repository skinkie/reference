from dataclasses import dataclass

from .common_vehicle_service_version_structure import CommonVehicleServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommonVehicleService1(CommonVehicleServiceVersionStructure):
    class Meta:
        name = "CommonVehicleService"
        namespace = "http://www.netex.org.uk/netex"
