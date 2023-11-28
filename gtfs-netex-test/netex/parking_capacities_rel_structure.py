from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.parking_capacity import ParkingCapacity
from netex.parking_capacity_ref import ParkingCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingCapacitiesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING CAPACITies.
    """
    class Meta:
        name = "parkingCapacities_RelStructure"

    parking_capacity_ref_or_parking_capacity: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingCapacityRef",
                    "type": ParkingCapacityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingCapacity",
                    "type": ParkingCapacity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
