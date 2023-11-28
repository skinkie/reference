from dataclasses import dataclass, field
from typing import List
from netex.assistance_booking_service import AssistanceBookingService
from netex.assistance_booking_service_ref import AssistanceBookingServiceRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AssistanceBookingServicesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ASSISTANCE BOOKING SERVICEs.
    """
    class Meta:
        name = "assistanceBookingServices_RelStructure"

    assistance_booking_service_ref_or_assistance_booking_service: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
