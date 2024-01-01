from dataclasses import dataclass
from .assistance_booking_service_version_structure import (
    AssistanceBookingServiceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceBookingService(AssistanceBookingServiceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
