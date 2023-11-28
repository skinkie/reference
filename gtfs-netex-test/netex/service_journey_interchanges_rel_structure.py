from dataclasses import dataclass, field
from typing import List
from netex.service_journey_interchange import ServiceJourneyInterchange
from netex.service_journey_interchange_ref import ServiceJourneyInterchangeRef
from netex.service_journey_interchange_view import ServiceJourneyInterchangeView
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceJourneyInterchangesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of SERVICE JOURNEY INTERCHANGE.
    """
    class Meta:
        name = "serviceJourneyInterchanges_RelStructure"

    service_journey_interchange_ref_or_service_journey_interchange_or_service_journey_interchange_view: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyInterchangeRef",
                    "type": ServiceJourneyInterchangeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchangeView",
                    "type": ServiceJourneyInterchangeView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
