from dataclasses import dataclass

from .vehicle_type_preference_versioned_child_structure import VehicleTypePreferenceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleTypePreference(VehicleTypePreferenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
