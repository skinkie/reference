from dataclasses import dataclass
from .journey_meeting_derived_view_structure import (
    JourneyMeetingDerivedViewStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyMeetingView(JourneyMeetingDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
