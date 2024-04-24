from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .luggage_spot import LuggageSpot
from .luggage_spot_ref import LuggageSpotRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageSpotsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "luggageSpots_RelStructure"

    luggage_spot_ref_or_luggage_spot: List[Union[LuggageSpotRef, LuggageSpot]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LuggageSpotRef",
                    "type": LuggageSpotRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageSpot",
                    "type": LuggageSpot,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
