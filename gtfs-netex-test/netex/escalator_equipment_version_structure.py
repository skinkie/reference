from dataclasses import dataclass, field
from typing import Optional
from netex.stair_equipment_version_structure import StairEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EscalatorEquipmentVersionStructure(StairEquipmentVersionStructure):
    """
    Type for an ESCALATOR EQUIPMENT.

    :ivar tactile_actuators: Whether ESCALATOR has a tactile actuator.
    :ivar energy_saving: Whether ESCALATOR is Energy Saving.
    :ivar dogs_must_be_carried: Whether dogs must be carried on
        ESCALATOR. +v1.1
    :ivar escalator_with_landing: Whether ESCALATOR has a landing. +v1.1
    """
    class Meta:
        name = "EscalatorEquipment_VersionStructure"

    tactile_actuators: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    energy_saving: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnergySaving",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    dogs_must_be_carried: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DogsMustBeCarried",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    escalator_with_landing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EscalatorWithLanding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
