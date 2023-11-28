from dataclasses import dataclass, field
from typing import Optional
from netex.journey_run_times_rel_structure import JourneyRunTimesRelStructure
from netex.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.service_link_ref import ServiceLinkRef
from netex.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkInJourneyPatternVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    """
    Type for a SERVICE LINK IN JOURNEY PATTERN.

    :ivar timing_link_ref:
    :ivar run_times: run times for this TIMING LINK.
    :ivar service_link_ref:
    """
    class Meta:
        name = "ServiceLinkInJourneyPattern_VersionedChildStructure"

    timing_link_ref: Optional[TimingLinkRef] = field(
        default=None,
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    run_times: Optional[JourneyRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_link_ref: ServiceLinkRef = field(
        metadata={
            "name": "ServiceLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
