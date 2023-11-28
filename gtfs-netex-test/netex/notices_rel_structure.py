from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.notice import Notice
from netex.notice_ref import NoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of NOTICEs.
    """
    class Meta:
        name = "notices_RelStructure"

    notice_ref_or_notice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "NoticeRef",
                    "type": NoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Notice",
                    "type": Notice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
