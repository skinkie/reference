from dataclasses import dataclass, field
from netex.car_model_profile_version_structure import CarModelProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CarModelProfile(CarModelProfileVersionStructure):
    """A set of characteristics of equipment installed on-board and characterising
    a CAR MODEL PROFILE.

    +v1.2.2

    :ivar id: Identifier of CAR MODEL PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
