from dataclasses import dataclass

from .observed_passing_time_view_structure import ObservedPassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ObservedPassingTimeView(ObservedPassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
