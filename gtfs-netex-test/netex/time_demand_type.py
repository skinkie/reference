from dataclasses import dataclass
from .time_demand_type_version_structure import TimeDemandTypeVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandType(TimeDemandTypeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
