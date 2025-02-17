from dataclasses import dataclass, field
from typing import Union

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .recharging_equipment_profile_ref import RechargingEquipmentProfileRef
from .vehicle_equipment_profile_ref import VehicleEquipmentProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleEquipmentProfileRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "vehicleEquipmentProfileRefs_RelStructure"

    vehicle_equipment_profile_ref: list[Union[RechargingEquipmentProfileRef, VehicleEquipmentProfileRef]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RechargingEquipmentProfileRef",
                    "type": RechargingEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfileRef",
                    "type": VehicleEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
