from dataclasses import dataclass
from netex.dead_run_journey_pattern_ref_structure import DeadRunJourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRunJourneyPatternRef(DeadRunJourneyPatternRefStructure):
    """
    Reference to a DEAD RUN JOURNEY PATTERN.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
