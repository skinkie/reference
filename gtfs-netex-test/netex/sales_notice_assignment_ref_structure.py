from dataclasses import dataclass

from .notice_assignment_ref_structure import NoticeAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SalesNoticeAssignmentRefStructure(NoticeAssignmentRefStructure):
    pass
