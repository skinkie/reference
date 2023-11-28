from dataclasses import dataclass
from netex.vehicle_entrance_ref_structure import VehicleEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEntranceRef(VehicleEntranceRefStructure):
    """
    Reference to an VEHICLE ENTRANCE to a SITE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
