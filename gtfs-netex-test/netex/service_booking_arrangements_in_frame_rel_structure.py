from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_booking_arrangement import ServiceBookingArrangement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceBookingArrangementsInFrameRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "serviceBookingArrangementsInFrame_RelStructure"

    service_booking_arrangement: List[ServiceBookingArrangement] = field(
        default_factory=list,
        metadata={
            "name": "ServiceBookingArrangement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
