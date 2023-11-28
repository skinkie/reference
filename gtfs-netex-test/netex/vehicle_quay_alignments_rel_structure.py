from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_quay_alignment import VehicleQuayAlignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleQuayAlignmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE QUAY ALIGNMENTs.
    """
    class Meta:
        name = "vehicleQuayAlignments_RelStructure"

    vehicle_quay_alignment: List[VehicleQuayAlignment] = field(
        default_factory=list,
        metadata={
            "name": "VehicleQuayAlignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
