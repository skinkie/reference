from dataclasses import dataclass, field
from typing import Optional

from .stair_equipment_version_structure import StairEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class EscalatorEquipmentVersionStructure(StairEquipmentVersionStructure):
    class Meta:
        name = "EscalatorEquipment_VersionStructure"

    tactile_actuators: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    energy_saving: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnergySaving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dogs_must_be_carried: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DogsMustBeCarried",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    escalator_with_landing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EscalatorWithLanding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    monitoring_remote_control: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MonitoringRemoteControl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
