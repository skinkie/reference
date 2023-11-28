from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.flexible_area_ref import FlexibleAreaRef
from netex.flexible_quay import FlexibleQuay
from netex.flexible_quay_ref import FlexibleQuayRef
from netex.hail_and_ride_area_ref import HailAndRideAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleQuaysRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FLEXIBLE QUAYs.
    """
    class Meta:
        name = "flexibleQuays_RelStructure"

    choice: List[object] = field(
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
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuay",
                    "type": FlexibleQuay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
