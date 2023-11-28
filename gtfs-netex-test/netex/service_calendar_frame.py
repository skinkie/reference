from dataclasses import dataclass, field
from netex.service_calendar_frame_version_frame_structure import ServiceCalendarFrameVersionFrameStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceCalendarFrame(ServiceCalendarFrameVersionFrameStructure):
    """A SERVICE CALENDAR.

    A coherent set of OPERATING DAYS and DAY TYPES comprising a
    Calendar.  that may be used to state the temporal VALIDITY of other
    NeTEx entities such as Timetables, STOP PLACEs, etc. Covers a PERIOD
    with a collection of assignments of OPERATING DAYS to DAY TYPES.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
