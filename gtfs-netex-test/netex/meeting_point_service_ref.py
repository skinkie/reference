from dataclasses import dataclass
from .meeting_point_service_ref_structure import (
    MeetingPointServiceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingPointServiceRef(MeetingPointServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
