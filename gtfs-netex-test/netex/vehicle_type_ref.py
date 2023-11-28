from dataclasses import dataclass
from netex.vehicle_type_ref_structure import VehicleTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypeRef(VehicleTypeRefStructure):
    """
    Reference to a VEHICLE TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
