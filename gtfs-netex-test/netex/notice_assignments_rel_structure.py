from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.notice_assignment import NoticeAssignment
from netex.notice_assignment_view import NoticeAssignmentView
from netex.sales_notice_assignment import SalesNoticeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticeAssignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of NOTICE ASSIGNMENTs.
    """
    class Meta:
        name = "noticeAssignments_RelStructure"

    sales_notice_assignment_or_notice_assignment_or_notice_assignment_view: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesNoticeAssignment",
                    "type": SalesNoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignment",
                    "type": NoticeAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NoticeAssignmentView",
                    "type": NoticeAssignmentView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
