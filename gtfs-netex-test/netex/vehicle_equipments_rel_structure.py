from dataclasses import dataclass, field
from typing import List, Union
from .access_vehicle_equipment import AccessVehicleEquipment
from .containment_aggregation_structure import ContainmentAggregationStructure
from .wheelchair_vehicle_equipment import WheelchairVehicleEquipment


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "vehicleEquipments_RelStructure"

    access_vehicle_equipment_or_wheelchair_vehicle_equipment: List[
        Union[AccessVehicleEquipment, WheelchairVehicleEquipment]
    ] = field(
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
        },
    )
