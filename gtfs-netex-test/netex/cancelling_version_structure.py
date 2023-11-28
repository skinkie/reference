from dataclasses import dataclass, field
from typing import Optional
from netex.booking_arrangements_structure import BookingArrangementsStructure
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CancellingVersionStructure(UsageParameterVersionStructure):
    """
    Type for CANCELLING.

    :ivar booking_arrangements: Booking Arrangements for Cancellations.
    :ivar cancellation_allowed: Whether Cancellation is allowed. +v1.2.2
    :ivar booking_deposit_refundable: Whether a booking deposit is
        refunded on cancellation.
    """
    class Meta:
        name = "Cancelling_VersionStructure"

    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancellation_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancellationAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_deposit_refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BookingDepositRefundable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
