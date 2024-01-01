from dataclasses import dataclass
from .point_in_journey_pattern_ref_structure import (
    PointInJourneyPatternRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPointInJourneyPatternRefStructure(PointInJourneyPatternRefStructure):
    value: RestrictedVar
