from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_entrance_ref import VehicleEntranceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEntrancesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE ENTRANCEs.
    """
    class Meta:
        name = "vehicleEntrances_RelStructure"

    vehicle_entrance_ref: List[VehicleEntranceRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleEntranceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
