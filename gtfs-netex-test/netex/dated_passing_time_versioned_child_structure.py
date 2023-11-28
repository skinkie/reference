from dataclasses import dataclass, field
from typing import Optional
from netex.journey_ref_structure import JourneyRefStructure
from netex.passing_time_versioned_child_structure import PassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedPassingTimeVersionedChildStructure(PassingTimeVersionedChildStructure):
    """
    Type for DATED PASSING TIME.

    :ivar dated_journey_ref: Dated journey for which this is the
        PASSING TIME. If given by context does not need to be restated.
    """
    class Meta:
        name = "DatedPassingTime_VersionedChildStructure"

    dated_journey_ref: Optional[JourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
