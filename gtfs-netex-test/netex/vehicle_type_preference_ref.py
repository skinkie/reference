from dataclasses import dataclass
from netex.vehicle_type_preference_ref_structure import VehicleTypePreferenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypePreferenceRef(VehicleTypePreferenceRefStructure):
    """
    Reference to a VEHICLE TYPE PREFERENCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
