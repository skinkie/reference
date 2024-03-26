from dataclasses import dataclass

from .service_booking_arrangement_ref_structure import (
    ServiceBookingArrangementRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceBookingArrangementRef(ServiceBookingArrangementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
