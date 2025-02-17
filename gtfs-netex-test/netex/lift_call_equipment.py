from dataclasses import dataclass

from .lift_call_equipment_version_structure import LiftCallEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LiftCallEquipment(LiftCallEquipmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
