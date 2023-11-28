from dataclasses import dataclass, field
from typing import List
from netex.charging_equipment_profile import ChargingEquipmentProfile
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingEquipmenProfilesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CHARGING EQUIPMENT PROFILEs.

    :ivar charging_equipment_profile: Charging equipment profile for
        VEHICLE.
    """
    class Meta:
        name = "chargingEquipmenProfilesInFrame_RelStructure"

    charging_equipment_profile: List[ChargingEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "ChargingEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
