from dataclasses import dataclass, field

from .service_booking_arrangement_version_structure import ServiceBookingArrangementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceBookingArrangement(ServiceBookingArrangementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
