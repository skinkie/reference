from dataclasses import dataclass, field
from typing import List, Optional

from .all_road_vehicle_category_enumeration import AllRoadVehicleCategoryEnumeration
from .deck_entrance_version_structure import DeckEntranceVersionStructure
from .vehicle_type_refs_rel_structure import VehicleTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckVehicleEntranceVersionStructure(DeckEntranceVersionStructure):
    class Meta:
        name = "DeckVehicleEntrance_VersionStructure"

    vehicle_types: Optional[VehicleTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_categories: List[AllRoadVehicleCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCategories",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
