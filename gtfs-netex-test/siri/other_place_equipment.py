from dataclasses import dataclass

from .place_equipment_structure import PlaceEquipmentStructure

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class OtherPlaceEquipment(PlaceEquipmentStructure):
    class Meta:
        namespace = "http://www.ifopt.org.uk/ifopt"
