from dataclasses import dataclass, field
from typing import Any

from .notice_assignment_derived_view_structure import NoticeAssignmentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentView(NoticeAssignmentDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
