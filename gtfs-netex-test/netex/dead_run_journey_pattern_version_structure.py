from dataclasses import dataclass

from .sections_in_sequence_rel_structure import JourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DeadRunJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    class Meta:
        name = "DeadRunJourneyPattern_VersionStructure"
