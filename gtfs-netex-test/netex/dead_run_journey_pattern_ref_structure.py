from dataclasses import dataclass
from netex.journey_pattern_ref_structure import JourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRunJourneyPatternRefStructure(JourneyPatternRefStructure):
    """
    Type for a reference to a DEAD RUN JOURNEY PATTERN.
    """
