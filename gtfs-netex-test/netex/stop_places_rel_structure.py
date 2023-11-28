from dataclasses import dataclass, field
from typing import Optional
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.stop_place import StopPlace
from netex.stop_place_ref import StopPlaceRef
from netex.taxi_rank_ref import TaxiRankRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of STOP PLACEs.
    """
    class Meta:
        name = "stopPlaces_RelStructure"

    taxi_rank_ref_or_stop_place_ref_or_stop_place: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TaxiRankRef",
                    "type": TaxiRankRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
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
