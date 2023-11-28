from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle import Vehicle
from netex.vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLEs.
    """
    class Meta:
        name = "vehicles_RelStructure"

    vehicle_ref_or_vehicle: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleRef",
                    "type": VehicleRef,
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
