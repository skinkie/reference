from dataclasses import dataclass
from .vehicle_type_preference_ref_structure import (
    VehicleTypePreferenceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleTypePreferenceRef(VehicleTypePreferenceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
