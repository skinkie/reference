from dataclasses import dataclass
from .time_interval_version_structure import TimeIntervalVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeInterval(TimeIntervalVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
