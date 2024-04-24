from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDuration, XmlTime

from .booking_access_enumeration import BookingAccessEnumeration
from .booking_arrangements_rel_structure import BookingArrangementsRelStructure
from .booking_method_enumeration import BookingMethodEnumeration
from .contact_structure import ContactStructure
from .flexible_line_type_enumeration import FlexibleLineTypeEnumeration
from .info_link_structure import InfoLinkStructure
from .line_derived_view_structure import LineDerivedViewStructure
from .multilingual_string import MultilingualString
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleLineDerivedViewStructure(LineDerivedViewStructure):
    class Meta:
        name = "FlexibleLine_DerivedViewStructure"

    flexible_line_type: Optional[FlexibleLineTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleLineType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: List[
        Union[
            ContactStructure,
            List[BookingMethodEnumeration],
            BookingAccessEnumeration,
            PurchaseWhenEnumeration,
            List[PurchaseMomentEnumeration],
            XmlTime,
            "FlexibleLineDerivedViewStructure.MinimumBookingPeriod",
            "FlexibleLineDerivedViewStructure.MaximumBookingPeriod",
            InfoLinkStructure,
            MultilingualString,
            BookingArrangementsRelStructure,
        ]
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
                    "type": ForwardRef("FlexibleLineDerivedViewStructure.MinimumBookingPeriod"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MaximumBookingPeriod",
                    "type": ForwardRef("FlexibleLineDerivedViewStructure.MaximumBookingPeriod"),
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
                {
                    "name": "bookingArrangements",
                    "type": BookingArrangementsRelStructure,
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
