from dataclasses import dataclass, field
from typing import Optional
from netex.link_in_link_sequence_versioned_child_structure import LinkInLinkSequenceVersionedChildStructure
from netex.service_link_ref import ServiceLinkRef
from netex.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LinkInJourneyPatternVersionedChildStructure(LinkInLinkSequenceVersionedChildStructure):
    """
    Type for LINK IN JOURNEY PATTERN.
    """
    class Meta:
        name = "LinkInJourneyPattern_VersionedChildStructure"

    service_link_ref_or_timing_link_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceLinkRef",
                    "type": ServiceLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
