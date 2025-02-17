from dataclasses import dataclass

from .time_demand_profile_version_structure import TimeDemandProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeDemandProfile(TimeDemandProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
