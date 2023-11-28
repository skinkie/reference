from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.hail_and_ride_area import HailAndRideArea
from netex.hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HailAndRideAreasRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of HAIL AND RIDE AREAs.
    """
    class Meta:
        name = "hailAndRideAreas_RelStructure"

    hail_and_ride_area_ref_or_hail_and_ride_area: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HailAndRideArea",
                    "type": HailAndRideArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
