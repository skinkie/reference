from dataclasses import dataclass, field
from typing import List
from netex.charging_equipment_profile_ref import ChargingEquipmentProfileRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.vehicle_equipment_profile_ref import VehicleEquipmentProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEquipmentProfileRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of VEHICLE EQUIPMENT PROFILEs.
    """
    class Meta:
        name = "vehicleEquipmentProfileRefs_RelStructure"

    charging_equipment_profile_ref_or_vehicle_equipment_profile_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ChargingEquipmentProfileRef",
                    "type": ChargingEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentProfileRef",
                    "type": VehicleEquipmentProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
