from dataclasses import dataclass, field
from netex.cycle_model_profile_version_structure import CycleModelProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleModelProfile(CycleModelProfileVersionStructure):
    """A set of characteristics of equipment installed on-board and characterising
    a CYCLE MODEL PROFILE.

    +v1.2.2

    :ivar id: Identifier of CYCLE MODEL PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
