from dataclasses import dataclass
from netex.car_model_profile_ref_structure import CarModelProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarModelProfileRef(CarModelProfileRefStructure):
    """Reference to a CAR MODEL PROFILE.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
