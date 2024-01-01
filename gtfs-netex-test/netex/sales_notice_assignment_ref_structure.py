from dataclasses import dataclass
from .notice_assignment_ref_structure import NoticeAssignmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesNoticeAssignmentRefStructure(NoticeAssignmentRefStructure):
    value: RestrictedVar
