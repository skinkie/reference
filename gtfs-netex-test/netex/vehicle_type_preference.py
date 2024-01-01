from dataclasses import dataclass
from .vehicle_type_preference_versioned_child_structure import (
    VehicleTypePreferenceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypePreference(VehicleTypePreferenceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
