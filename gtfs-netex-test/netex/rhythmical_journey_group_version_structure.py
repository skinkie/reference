from dataclasses import dataclass, field
from typing import Optional
from netex.journey_frequency_group_version_structure import JourneyFrequencyGroupVersionStructure
from netex.timeband_refs_rel_structure import TimebandRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RhythmicalJourneyGroupVersionStructure(JourneyFrequencyGroupVersionStructure):
    """
    Type for   Rhythmical JOURNEY GROUP.

    :ivar timebands: TIMEBANDS associated with JOURNEY FREQUENCY GROUP.
    """
    class Meta:
        name = "RhythmicalJourneyGroup_VersionStructure"

    timebands: Optional[TimebandRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
