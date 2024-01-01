from dataclasses import dataclass
from .target_passing_time_view_structure import TargetPassingTimeViewStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTimeView(TargetPassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
