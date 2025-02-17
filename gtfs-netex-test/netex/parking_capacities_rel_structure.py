from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .parking_capacity import ParkingCapacity
from .parking_capacity_ref import ParkingCapacityRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingCapacitiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "parkingCapacities_RelStructure"

    parking_capacity_ref_or_parking_capacity: list[Union[ParkingCapacityRef, ParkingCapacity]] = field(
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
        },
    )
