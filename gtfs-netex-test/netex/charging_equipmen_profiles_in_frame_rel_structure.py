from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .recharging_equipment_profile import RechargingEquipmentProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingEquipmenProfilesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "chargingEquipmenProfilesInFrame_RelStructure"

    recharging_equipment_profile: List[RechargingEquipmentProfile] = field(
        default_factory=list,
        metadata={
            "name": "RechargingEquipmentProfile",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
