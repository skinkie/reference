from dataclasses import dataclass, field
from typing import Optional
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.single_journey_refs_rel_structure import SingleJourneyRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfSingleJourneysVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a GROUP OF SINGLE JOURNEYs.

    :ivar members: Services in GROUP.
    :ivar notice_assignments: NOTICEs  relevant for the whole GROUP OF
        SINGLE JOURNEYs.
    """
    class Meta:
        name = "GroupOfSingleJourneys_VersionStructure"

    members: Optional[SingleJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
