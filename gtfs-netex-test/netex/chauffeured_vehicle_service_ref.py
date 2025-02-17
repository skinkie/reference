from dataclasses import dataclass

from .chauffeured_vehicle_service_ref_structure import ChauffeuredVehicleServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ChauffeuredVehicleServiceRef(ChauffeuredVehicleServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
