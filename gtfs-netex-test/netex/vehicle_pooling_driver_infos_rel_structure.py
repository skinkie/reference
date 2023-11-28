from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_pooling_driver_info import VehiclePoolingDriverInfo

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingDriverInfosRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of VEHICLE POOLING DRIVER INFOs.
    """
    class Meta:
        name = "vehiclePoolingDriverInfos_RelStructure"

    vehicle_pooling_driver_info: List[VehiclePoolingDriverInfo] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePoolingDriverInfo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
