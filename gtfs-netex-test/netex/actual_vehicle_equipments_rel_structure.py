from dataclasses import dataclass, field
from typing import List

from .actual_vehicle_equipment import ActualVehicleEquipment
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActualVehicleEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "actualVehicleEquipments_RelStructure"

    actual_vehicle_equipment: List[ActualVehicleEquipment] = field(
        default_factory=list,
        metadata={
            "name": "ActualVehicleEquipment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
