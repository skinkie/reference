from dataclasses import dataclass

from .booking_debit_ref_structure import BookingDebitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingDebitRef(BookingDebitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
