from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.stop_place_vehicle_entrance import StopPlaceVehicleEntrance
from netex.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StopPlaceVehicleEntrancesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of STOP PLACE VEHICLE ENTRANCEs.
    """
    class Meta:
        name = "stopPlaceVehicleEntrances_RelStructure"

    vehicle_entrance_ref_or_stop_place_vehicle_entrance: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleEntranceRef",
                    "type": VehicleEntranceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPlaceVehicleEntrance",
                    "type": StopPlaceVehicleEntrance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
