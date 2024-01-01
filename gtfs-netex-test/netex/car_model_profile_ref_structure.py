from dataclasses import dataclass
from .vehicle_model_profile_ref_structure import (
    VehicleModelProfileRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarModelProfileRefStructure(VehicleModelProfileRefStructure):
    value: RestrictedVar
