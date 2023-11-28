from dataclasses import dataclass
from netex.assistance_booking_service_ref_structure import AssistanceBookingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceBookingServiceRef(AssistanceBookingServiceRefStructure):
    """
    Reference to an ASSISTANCE BOOKING SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
