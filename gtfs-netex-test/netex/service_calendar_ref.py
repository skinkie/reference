from dataclasses import dataclass
from .service_calendar_ref_structure import ServiceCalendarRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceCalendarRef(ServiceCalendarRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
