from dataclasses import dataclass

from .assistance_booking_service_ref_structure import AssistanceBookingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AssistanceBookingServiceRef(AssistanceBookingServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
