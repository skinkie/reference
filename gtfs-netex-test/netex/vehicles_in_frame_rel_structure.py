from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.train_element import TrainElement
from netex.vehicle import Vehicle

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE TYPEs.
    """
    class Meta:
        name = "vehiclesInFrame_RelStructure"

    train_element_or_vehicle: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainElement",
                    "type": TrainElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Vehicle",
                    "type": Vehicle,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
