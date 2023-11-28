from dataclasses import dataclass, field
from netex.assistance_booking_service_version_structure import AssistanceBookingServiceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceBookingService(AssistanceBookingServiceVersionStructure):
    """
    Information about how to book assistance for wheelchair and disabled users.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
