from dataclasses import dataclass, field
from netex.meeting_restriction_version_structure import MeetingRestrictionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MeetingRestriction(MeetingRestrictionVersionStructure):
    """
    A pair of INFRASTRUCTURE LINKs where vehicles of specified VEHICLE TYPEs are
    not allowed to meet.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
