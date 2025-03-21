from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .vehicle_service_part import VehicleServicePart
from .vehicle_service_part_ref import VehicleServicePartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleServicePartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleServiceParts_RelStructure"

    vehicle_service_part_ref_or_vehicle_service_part: list[Union[VehicleServicePartRef, VehicleServicePart]] = field(
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
        },
    )
