from dataclasses import dataclass
from .meeting_point_service_version_structure import (
    MeetingPointServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MeetingPointService(MeetingPointServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
