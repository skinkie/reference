from dataclasses import dataclass, field
from typing import Union

from .booking_arrangement import BookingArrangement
from .booking_arrangement_ref import BookingArrangementRef
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingArrangementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "bookingArrangements_RelStructure"

    booking_arrangement_ref_or_booking_arrangement: list[Union[BookingArrangementRef, BookingArrangement]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BookingArrangementRef",
                    "type": BookingArrangementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BookingArrangement",
                    "type": BookingArrangement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
