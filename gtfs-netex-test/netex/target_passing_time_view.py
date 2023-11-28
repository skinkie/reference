from dataclasses import dataclass
from netex.target_passing_time_view_structure import TargetPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TargetPassingTimeView(TargetPassingTimeViewStructure):
    """
    Simplified TARGET PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
