from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.booking_access_enumeration import BookingAccessEnumeration
from netex.booking_method_enumeration import BookingMethodEnumeration
from netex.contact_structure import ContactStructure
from netex.multilingual_string import MultilingualString
from netex.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.purchase_when_enumeration import PurchaseWhenEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BookingArrangementsStructure:
    """
    Type for BOOKING ARRANGEMENTs.

    :ivar booking_contact: Contact for Booking. +v1.1
    :ivar booking_methods: Allowed Ways of Making a BOOKING.
    :ivar booking_access: Who can make a booking. Default is public.
    :ivar book_when: When Booking can be made. +V1.1
    :ivar buy_when: When purchase can be made.  +V1.1
    :ivar latest_booking_time: Latest time in day that booking can be
        made.
    :ivar minimum_booking_period: Minimum interval in advance of
        departure day or time that Service may be ordered.
    :ivar maximum_booking_period: Maximum interval in advance of
        departure day or time that Service may be ordered. +V1.2..2
    :ivar booking_url: URL for booking. +V1.1
    :ivar booking_note: Note about booking the FLEXIBLE LINE.
    """
    booking_contact: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_methods: List[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    booking_access: Optional[BookingAccessEnumeration] = field(
        default=None,
        metadata={
            "name": "BookingAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    book_when: Optional[PurchaseWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "BookWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    buy_when: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BuyWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    latest_booking_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestBookingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "BookingNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
