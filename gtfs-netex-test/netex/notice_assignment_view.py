from dataclasses import dataclass
from .notice_assignment_derived_view_structure import (
    NoticeAssignmentDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentView(NoticeAssignmentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name: RestrictedVar
