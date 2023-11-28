from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.notice_assignment_view import NoticeAssignmentView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticeAssignmentViewsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of NOTICE ASSIGNMENT VIEWs.
    """
    class Meta:
        name = "noticeAssignmentViews_RelStructure"

    notice_assignment_view: List[NoticeAssignmentView] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignmentView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
