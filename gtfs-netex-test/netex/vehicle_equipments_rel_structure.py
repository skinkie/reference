from dataclasses import dataclass, field
from typing import List
from netex.access_vehicle_equipment import AccessVehicleEquipment
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.wheelchair_vehicle_equipment import WheelchairVehicleEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    List of VEHICLE EQUIPMENT.
    """
    class Meta:
        name = "vehicleEquipments_RelStructure"

    access_vehicle_equipment_or_wheelchair_vehicle_equipment: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessVehicleEquipment",
                    "type": AccessVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleEquipment",
                    "type": WheelchairVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
