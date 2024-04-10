from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .recharging_equipment_profile import RechargingEquipmentProfile
from .vehicle_equipment_profile import VehicleEquipmentProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmenProfilesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleEquipmenProfilesInFrame_RelStructure"

    vehicle_equipment_profile_or_recharging_equipment_profile: List[Union[VehicleEquipmentProfile, RechargingEquipmentProfile]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleEquipmentProfile",
                    "type": VehicleEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RechargingEquipmentProfile",
                    "type": RechargingEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
