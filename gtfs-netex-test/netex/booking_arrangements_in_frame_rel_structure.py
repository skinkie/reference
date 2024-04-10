from dataclasses import dataclass, field
from typing import List

from .booking_arrangement import BookingArrangement
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingArrangementsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "bookingArrangementsInFrame_RelStructure"

    booking_arrangement: List[BookingArrangement] = field(
        default_factory=list,
        metadata={
            "name": "BookingArrangement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
