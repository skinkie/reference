from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure
from netex.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyRunTimeVersionedChildStructure(JourneyTimingVersionedChildStructure):
    """
    Type for JOURNEY RUN TIME.

    :ivar timing_link_ref:
    :ivar run_time: RUN TIME as an interval.
    """
    class Meta:
        name = "JourneyRunTime_VersionedChildStructure"

    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_time: XmlDuration = field(
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
