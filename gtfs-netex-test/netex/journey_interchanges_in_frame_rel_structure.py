from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.service_journey_interchange import ServiceJourneyInterchange
from netex.service_journey_pattern_interchange import ServiceJourneyPatternInterchange

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyInterchangesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  JOURNEY  INTERCHANGEs.
    """
    class Meta:
        name = "journeyInterchangesInFrame_RelStructure"

    service_journey_pattern_interchange_or_service_journey_interchange: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternInterchange",
                    "type": ServiceJourneyPatternInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyInterchange",
                    "type": ServiceJourneyInterchange,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
