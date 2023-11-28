from dataclasses import dataclass
from netex.estimated_passing_time_view_structure import EstimatedPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EstimatedPassingTimeView(EstimatedPassingTimeViewStructure):
    """
    Simplified ESTIMATED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
