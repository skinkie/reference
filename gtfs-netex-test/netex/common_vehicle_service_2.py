from dataclasses import dataclass

from .equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CommonVehicleService2(EquipmentVersionStructure):
    class Meta:
        name = "CommonVehicleService_"
        namespace = "http://www.netex.org.uk/netex"
