from dataclasses import dataclass
from .scheduled_stop_point_version_structure import (
    ScheduledStopPointVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledStopPoint(ScheduledStopPointVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
