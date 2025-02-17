from dataclasses import dataclass, field
from typing import Optional, Union

from .booking_arrangements_rel_structure import BookingArrangementsRelStructure
from .booking_arrangements_structure import BookingArrangementsStructure
from .usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CancellingVersionStructure(UsageParameterVersionStructure):
    class Meta:
        name = "Cancelling_VersionStructure"

    booking_arrangements_or_booking_arrangements: Optional[Union[BookingArrangementsRelStructure, BookingArrangementsStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "bookingArrangements",
                    "type": BookingArrangementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingArrangements",
                    "type": BookingArrangementsStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    cancellation_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancellationAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_deposit_refundable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BookingDepositRefundable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
