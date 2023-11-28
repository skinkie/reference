from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.flexible_stop_place import FlexibleStopPlace
from netex.flexible_stop_place_ref import FlexibleStopPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleStopPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FLEXIBLE STOP PLACEs.
    """
    class Meta:
        name = "flexibleStopPlaces_RelStructure"

    flexible_stop_place_ref_or_flexible_stop_place: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleStopPlaceRef",
                    "type": FlexibleStopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopPlace",
                    "type": FlexibleStopPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
