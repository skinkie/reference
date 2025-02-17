from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .service_booking_arrangement import ServiceBookingArrangement
from .service_booking_arrangement_ref import ServiceBookingArrangementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceBookingArrangementsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceBookingArrangements_RelStructure"

    service_booking_arrangement_ref_or_service_booking_arrangement: list[Union[ServiceBookingArrangementRef, ServiceBookingArrangement]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceBookingArrangementRef",
                    "type": ServiceBookingArrangementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceBookingArrangement",
                    "type": ServiceBookingArrangement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
