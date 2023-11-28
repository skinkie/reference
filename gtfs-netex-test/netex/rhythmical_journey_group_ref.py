from dataclasses import dataclass
from netex.rhythmical_journey_group_ref_structure import RhythmicalJourneyGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RhythmicalJourneyGroupRef(RhythmicalJourneyGroupRefStructure):
    """
    Reference to a RHYTHMICAL JOURNEY GROUP.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
