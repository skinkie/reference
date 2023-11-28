from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_service_part import VehicleServicePart
from netex.vehicle_service_part_ref import VehicleServicePartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicePartsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE SERVICE PARTs.
    """
    class Meta:
        name = "vehicleServiceParts_RelStructure"

    vehicle_service_part_ref_or_vehicle_service_part: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleServicePartRef",
                    "type": VehicleServicePartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleServicePart",
                    "type": VehicleServicePart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
