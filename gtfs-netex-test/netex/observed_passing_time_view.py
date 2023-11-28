from dataclasses import dataclass
from netex.observed_passing_time_view_structure import ObservedPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ObservedPassingTimeView(ObservedPassingTimeViewStructure):
    """
    Simplified OBSERVED PASSING TIME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
