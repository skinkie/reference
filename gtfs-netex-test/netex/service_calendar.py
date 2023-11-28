from dataclasses import dataclass, field
from netex.service_calendar_version_structure import ServiceCalendarVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceCalendar(ServiceCalendarVersionStructure):
    """A SERVICE CALENDAR.

    A collection of DAY TYPE ASSIGNMENTs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
