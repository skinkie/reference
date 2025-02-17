from dataclasses import dataclass

from .booking_arrangement_ref_structure import BookingArrangementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class BookingArrangementRef(BookingArrangementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
