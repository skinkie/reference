from dataclasses import dataclass
from .service_calendar_frame_ref_structure import (
    ServiceCalendarFrameRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendarFrameRef(ServiceCalendarFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
