from dataclasses import dataclass, field

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .vehicle_type_preference import VehicleTypePreference

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleTypePreferencesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vehicleTypePreferences_RelStructure"

    vehicle_type_preference: list[VehicleTypePreference] = field(
        default_factory=list,
        metadata={
            "name": "VehicleTypePreference",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
