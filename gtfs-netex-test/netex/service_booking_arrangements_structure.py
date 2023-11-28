from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.booking_arrangements_structure import BookingArrangementsStructure
from netex.booking_charge_type_enumeration import BookingChargeTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceBookingArrangementsStructure(BookingArrangementsStructure):
    """
    Type for SERVICE BOOKING ARRANGEMENTs.

    :ivar minimum_booking_duration: Minimum period for which a booking
        can be mad +v.1.2.2
    :ivar maximum_booking_duration: Maximum period for which a booking
        can be mad +v.1.2.2
    :ivar deposit_required: Whether a deposit is required. +v1.2.2
    :ivar booking_charge_type: Nature of booking fee. v1.2.2
    """
    minimum_booking_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_booking_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumBookingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    deposit_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DepositRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_charge_type: Optional[BookingChargeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BookingChargeType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
