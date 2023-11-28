from dataclasses import dataclass
from netex.time_demand_profile_ref_structure import TimeDemandProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandProfileRef(TimeDemandProfileRefStructure):
    """
    Reference to a TIME DEMAND PROFILE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
