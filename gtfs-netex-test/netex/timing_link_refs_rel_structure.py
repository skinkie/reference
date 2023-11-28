from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.timing_link_ref import TimingLinkRef
from netex.timing_link_ref_by_value import TimingLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingLinkRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to TIMING LINKs.
    """
    class Meta:
        name = "timingLinkRefs_RelStructure"

    timing_link_ref_or_timing_link_ref_by_value: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimingLinkRef",
                    "type": TimingLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingLinkRefByValue",
                    "type": TimingLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
