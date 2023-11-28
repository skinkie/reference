from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_pattern_view import JourneyPatternView
from netex.service_pattern import ServicePattern

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServicePatternsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE PATTERNs.
    """
    class Meta:
        name = "servicePatternsInFrame_RelStructure"

    service_pattern_or_journey_pattern_view: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServicePattern",
                    "type": ServicePattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternView",
                    "type": JourneyPatternView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
