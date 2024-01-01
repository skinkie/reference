from dataclasses import dataclass
from .stop_point_in_journey_pattern_derived_view_structure import (
    StopPointInJourneyPatternDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPointInJourneyPatternView(
    StopPointInJourneyPatternDerivedViewStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
