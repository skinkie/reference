from dataclasses import dataclass
from netex.time_demand_profile_member_version_structure import TimeDemandProfileMemberVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandProfileMember(TimeDemandProfileMemberVersionStructure):
    """
    TIME DEMAND PROFILE member.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
