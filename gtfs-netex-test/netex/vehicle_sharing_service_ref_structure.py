from dataclasses import dataclass
from netex.common_vehicle_service_ref_structure import CommonVehicleServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingServiceRefStructure(CommonVehicleServiceRefStructure):
    """
    Type for a reference to an VEHICLE SHARING SERVICE.
    """
