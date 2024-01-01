from dataclasses import dataclass
from .journey_frequency_group_ref_structure import (
    JourneyFrequencyGroupRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RhythmicalJourneyGroupRefStructure(JourneyFrequencyGroupRefStructure):
    value: RestrictedVar
