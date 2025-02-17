from dataclasses import dataclass

from .service_calendar_frame_ref_structure import ServiceCalendarFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceCalendarFrameRef(ServiceCalendarFrameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
