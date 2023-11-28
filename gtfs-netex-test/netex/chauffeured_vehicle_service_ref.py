from dataclasses import dataclass
from netex.chauffeured_vehicle_service_ref_structure import ChauffeuredVehicleServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChauffeuredVehicleServiceRef(ChauffeuredVehicleServiceRefStructure):
    """Identifier of an CHAUFFEURED VEHICLE SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
