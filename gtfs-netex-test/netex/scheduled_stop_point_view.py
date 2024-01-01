from dataclasses import dataclass
from .scheduled_stop_point_derived_view_structure import (
    ScheduledStopPointDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledStopPointView(ScheduledStopPointDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
