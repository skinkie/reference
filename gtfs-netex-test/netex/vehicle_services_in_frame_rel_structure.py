from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_service import VehicleService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleServicesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleServicesInFrame_RelStructure"

    vehicle_service: list[VehicleService] = field(
        default_factory=list,
        metadata={
            "name": "VehicleService",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
