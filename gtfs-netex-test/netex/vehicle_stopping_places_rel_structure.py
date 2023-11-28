from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_stopping_place import VehicleStoppingPlace
from netex.vehicle_stopping_place_ref import VehicleStoppingPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleStoppingPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE STOPPING PLACEs.
    """
    class Meta:
        name = "vehicleStoppingPlaces_RelStructure"

    vehicle_stopping_place_ref_or_vehicle_stopping_place: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleStoppingPlaceRef",
                    "type": VehicleStoppingPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleStoppingPlace",
                    "type": VehicleStoppingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
