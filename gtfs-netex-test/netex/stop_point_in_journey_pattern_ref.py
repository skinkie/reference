from dataclasses import dataclass
from .stop_point_in_journey_pattern_ref_structure import (
    StopPointInJourneyPatternRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPointInJourneyPatternRef(StopPointInJourneyPatternRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
