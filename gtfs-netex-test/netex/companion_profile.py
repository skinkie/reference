from dataclasses import dataclass, field
from netex.companion_profile_version_structure import CompanionProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompanionProfile(CompanionProfileVersionStructure):
    """
    The number and characteristics (weight, volume) of luggage that a holder of an
    access right is entitled to carry.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
