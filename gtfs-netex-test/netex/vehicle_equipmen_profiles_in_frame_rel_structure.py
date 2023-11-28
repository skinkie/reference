from dataclasses import dataclass, field
from typing import List
from netex.charging_equipment_profile import ChargingEquipmentProfile
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_equipment_profile import VehicleEquipmentProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEquipmenProfilesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of VEHICLE EQUIPMENT PROFILEs.
    """
    class Meta:
        name = "vehicleEquipmenProfilesInFrame_RelStructure"

    vehicle_equipment_profile_or_charging_equipment_profile: List[object] = field(
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
                    "name": "ChargingEquipmentProfile",
                    "type": ChargingEquipmentProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
