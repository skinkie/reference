from dataclasses import dataclass, field

from .equipment_position import EquipmentPosition
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EquipmentPositionsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "equipmentPositions_RelStructure"

    equipment_position: list[EquipmentPosition] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
