from dataclasses import dataclass
from netex.service_calendar_ref_structure import ServiceCalendarRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceCalendarRef(ServiceCalendarRefStructure):
    """
    Reference to a SERVICE CALENDAR.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
