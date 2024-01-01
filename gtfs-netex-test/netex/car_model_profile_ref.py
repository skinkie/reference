from dataclasses import dataclass
from .car_model_profile_ref_structure import CarModelProfileRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CarModelProfileRef(CarModelProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
