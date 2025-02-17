from dataclasses import dataclass

from .common_vehicle_service_ref_structure import CommonVehicleServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommonVehicleServiceRef(CommonVehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
