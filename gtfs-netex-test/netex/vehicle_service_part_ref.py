from dataclasses import dataclass
from netex.vehicle_service_part_ref_structure import VehicleServicePartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePartRef(VehicleServicePartRefStructure):
    """
    Reference to a VEHICLE SERVICE PART.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
