from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.equipment_place import EquipmentPlace
from netex.equipment_place_ref import EquipmentPlaceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of EQUIPMENT PLACEs.
    """
    class Meta:
        name = "equipmentPlaces_RelStructure"

    equipment_place_ref_or_equipment_place: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EquipmentPlaceRef",
                    "type": EquipmentPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentPlace",
                    "type": EquipmentPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
