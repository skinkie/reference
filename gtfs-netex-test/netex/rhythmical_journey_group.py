from dataclasses import dataclass
from .rhythmical_journey_group_version_structure import (
    RhythmicalJourneyGroupVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RhythmicalJourneyGroup(RhythmicalJourneyGroupVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
