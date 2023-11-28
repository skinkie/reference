from dataclasses import dataclass
from netex.meeting_restriction_ref_structure import MeetingRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MeetingRestrictionRef(MeetingRestrictionRefStructure):
    """
    Reference to a MEETING RESTRICTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
