from dataclasses import dataclass

from .ramp_equipment_version_structure import RampEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RampEquipment(RampEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
