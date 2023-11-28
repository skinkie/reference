from dataclasses import dataclass
from netex.vehicle_model_ref_structure import VehicleModelRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleModelRef(VehicleModelRefStructure):
    """
    Reference to a VEHICLE MODEL.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
