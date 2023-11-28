from dataclasses import dataclass, field
from netex.time_demand_profile_version_structure import TimeDemandProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandProfile(TimeDemandProfileVersionStructure):
    """
    TIME DEMAND PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
