from dataclasses import dataclass
from .service_calendar_frame_version_frame_structure import (
    ServiceCalendarFrameVersionFrameStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendarFrame(ServiceCalendarFrameVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
