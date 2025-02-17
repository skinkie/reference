from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .notice_assignment_view import NoticeAssignmentView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class NoticeAssignmentViewsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "noticeAssignmentViews_RelStructure"

    notice_assignment_view: list[NoticeAssignmentView] = field(
        default_factory=list,
        metadata={
            "name": "NoticeAssignmentView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
