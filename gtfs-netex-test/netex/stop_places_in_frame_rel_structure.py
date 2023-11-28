from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.stop_place import StopPlace
from netex.taxi_rank import TaxiRank

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlacesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of STOP PLACE.
    """
    class Meta:
        name = "stopPlacesInFrame_RelStructure"

    taxi_rank_or_stop_place: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRank",
                    "type": TaxiRank,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlace",
                    "type": StopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
