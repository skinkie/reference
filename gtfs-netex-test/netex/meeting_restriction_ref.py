from dataclasses import dataclass
from .meeting_restriction_ref_structure import MeetingRestrictionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingRestrictionRef(MeetingRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
