from dataclasses import dataclass, field
from typing import Optional
from netex.equipment_positions_rel_structure import EquipmentPositionsRelStructure
from netex.equipments_rel_structure import EquipmentsRelStructure
from netex.site_element_version_structure import SiteElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EquipmentPlaceVersionStructure(SiteElementVersionStructure):
    """
    Type for an EQUIPMENT PLACE.

    :ivar equipment_positions: Positions of EQUIPMENT.
    :ivar place_equipments: Items of EQUIPMENT that may be located in an
        EQUIPMENT PLACE.
    """
    class Meta:
        name = "EquipmentPlace_VersionStructure"

    equipment_positions: Optional[EquipmentPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
