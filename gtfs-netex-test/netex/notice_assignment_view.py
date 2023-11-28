from dataclasses import dataclass
from netex.notice_assignment_derived_view_structure import NoticeAssignmentDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NoticeAssignmentView(NoticeAssignmentDerivedViewStructure):
    """View of a NOTICE ASSIGNMENT.

    for use in a specific context such as a CALL. This can be used to
    embed the notice itself in the context.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
