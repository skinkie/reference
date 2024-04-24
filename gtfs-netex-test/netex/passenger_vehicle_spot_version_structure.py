from dataclasses import dataclass, field
from typing import List, Optional

from .all_road_vehicle_category_enumeration import AllRoadVehicleCategoryEnumeration
from .locatable_spot_version_structure import LocatableSpotVersionStructure
from .transport_type_refs_rel_structure import TransportTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleSpotVersionStructure(LocatableSpotVersionStructure):
    class Meta:
        name = "PassengerVehicleSpot_VersionStructure"

    vehicle_categories: List[AllRoadVehicleCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCategories",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    transport_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "transportTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
