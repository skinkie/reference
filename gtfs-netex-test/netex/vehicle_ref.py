from dataclasses import dataclass
from netex.vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRef(VehicleRefStructure):
    """
    Reference to a VEHICLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
