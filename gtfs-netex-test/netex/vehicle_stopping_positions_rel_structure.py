from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_stopping_position import VehicleStoppingPosition
from netex.vehicle_stopping_position_ref import VehicleStoppingPositionRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPositionsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE STOPPING POSITIONs.
    """
    class Meta:
        name = "vehicleStoppingPositions_RelStructure"

    vehicle_stopping_position_ref_or_vehicle_stopping_position: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleStoppingPositionRef",
                    "type": VehicleStoppingPositionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPosition",
                    "type": VehicleStoppingPosition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
