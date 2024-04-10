from dataclasses import dataclass

from .booking_arrangement_ref_structure import BookingArrangementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceBookingArrangementRefStructure(BookingArrangementRefStructure):
    pass
