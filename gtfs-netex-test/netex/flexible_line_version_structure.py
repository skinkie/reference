from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .booking_access_enumeration import BookingAccessEnumeration
from .booking_method_enumeration import BookingMethodEnumeration
from .contact_structure import ContactStructure
from .flexible_line_type_enumeration import FlexibleLineTypeEnumeration
from .info_link_structure import InfoLinkStructure
from .line_version_structure import LineVersionStructure
from .multilingual_string import MultilingualString
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineVersionStructure(LineVersionStructure):
    class Meta:
        name = "FlexibleLine_VersionStructure"

    flexible_line_type: Optional[FlexibleLineTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleLineType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_contact_or_booking_methods_or_booking_access_or_book_when_or_buy_when_or_latest_booking_time_or_minimum_booking_period_or_maximum_booking_period_or_booking_url_or_booking_note: List[
        Union[ContactStructure, List[BookingMethodEnumeration], BookingAccessEnumeration, PurchaseWhenEnumeration, List[PurchaseMomentEnumeration], XmlTime, "FlexibleLineVersionStructure.MinimumBookingPeriod", "FlexibleLineVersionStructure.MaximumBookingPeriod", InfoLinkStructure, MultilingualString]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BookingContact",
                    "type": ContactStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingMethods",
                    "type": List[BookingMethodEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "BookingAccess",
                    "type": BookingAccessEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookWhen",
                    "type": PurchaseWhenEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BuyWhen",
                    "type": List[PurchaseMomentEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "LatestBookingTime",
                    "type": XmlTime,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumBookingPeriod",
                    "type": ForwardRef("FlexibleLineVersionStructure.MinimumBookingPeriod"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MaximumBookingPeriod",
                    "type": ForwardRef("FlexibleLineVersionStructure.MaximumBookingPeriod"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingUrl",
                    "type": InfoLinkStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingNote",
                    "type": MultilingualString,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 10,
        },
    )

    @dataclass(kw_only=True)
    class MinimumBookingPeriod:
        value: XmlDuration = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class MaximumBookingPeriod:
        value: XmlDuration = field(
            metadata={
                "required": True,
            }
        )
