from dataclasses import dataclass
from .estimated_passing_time_view_structure import (
    EstimatedPassingTimeViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTimeView(EstimatedPassingTimeViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
