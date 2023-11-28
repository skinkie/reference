from dataclasses import dataclass, field
from typing import List
from netex.equipment_position import EquipmentPosition
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPositionsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of EQUIPMENT POSITIONs.
    """
    class Meta:
        name = "equipmentPositions_RelStructure"

    equipment_position: List[EquipmentPosition] = field(
        default_factory=list,
        metadata={
            "name": "EquipmentPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
