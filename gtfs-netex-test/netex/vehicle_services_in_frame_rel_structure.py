from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_service import VehicleService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleServicesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE SERVICEs.
    """
    class Meta:
        name = "vehicleServicesInFrame_RelStructure"

    vehicle_service: List[VehicleService] = field(
        default_factory=list,
        metadata={
            "name": "VehicleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
