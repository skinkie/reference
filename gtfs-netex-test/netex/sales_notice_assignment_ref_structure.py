from dataclasses import dataclass
from netex.notice_assignment_ref_structure import NoticeAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SalesNoticeAssignmentRefStructure(NoticeAssignmentRefStructure):
    """
    Type for Reference to a SALES NOTICE ASSIGNMENT.
    """
