from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.railway_element import RailwayElement
from netex.road_element import RoadElement
from netex.wire_element import WireElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InfrastructureElementsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of INFRASTRUCTURE LINKs.
    """
    class Meta:
        name = "infrastructureElementsInFrame_RelStructure"

    railway_element_or_road_element_or_wire_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RailwayElement",
                    "type": RailwayElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoadElement",
                    "type": RoadElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WireElement",
                    "type": WireElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
