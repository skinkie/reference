from dataclasses import dataclass

from .time_demand_type_version_structure import TimeDemandTypeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeDemandType(TimeDemandTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
