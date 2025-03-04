from dataclasses import dataclass

from .time_interval_version_structure import TimeIntervalVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeInterval(TimeIntervalVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
