from dataclasses import dataclass
from netex.journey_frequency_group_ref_structure import JourneyFrequencyGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RhythmicalJourneyGroupRefStructure(JourneyFrequencyGroupRefStructure):
    """
    Type for a reference to a RHYTHMICAL JOURNEY GROUP.
    """
