from dataclasses import dataclass, field
from typing import List
from netex.activation_point import ActivationPoint
from netex.beacon_point import BeaconPoint
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationPointsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ACTIVATION POINTs.
    """
    class Meta:
        name = "activationPointsInFrame_RelStructure"

    beacon_point_or_activation_point: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "BeaconPoint",
                    "type": BeaconPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivationPoint",
                    "type": ActivationPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
