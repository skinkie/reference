from dataclasses import dataclass
from netex.passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassingTimeView(PassingTimeViewStructure):
    """
    Simplified TARGET PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
