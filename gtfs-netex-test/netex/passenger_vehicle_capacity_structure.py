from dataclasses import dataclass, field
from typing import List, Optional

from .all_road_vehicle_category_enumeration import AllRoadVehicleCategoryEnumeration
from .entity_in_version_structure import DataManagedObjectStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerVehicleCapacityStructure(DataManagedObjectStructure):
    vehicle_category: List[AllRoadVehicleCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleCategory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "VehicleCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
