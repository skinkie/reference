from dataclasses import dataclass

from .wheelchair_vehicle_ref_structure import WheelchairVehicleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class WheelchairVehicleEquipmentRef(WheelchairVehicleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
