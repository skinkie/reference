from dataclasses import dataclass
from netex.section_in_sequence_versioned_child_structure import JourneyPatternVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRunJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    """
    Type for DEAD RUN JOURNEY PATTERN.
    """
    class Meta:
        name = "DeadRunJourneyPattern_VersionStructure"
