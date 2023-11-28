from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelatorEquipmentVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for a TRAVELATOR EQUIPMENT.

    :ivar tactile_actuators: Whether Travelator has a tactile actuator.
    :ivar energy_saving: Whether Travelator is Energy Saving.
    :ivar speed: Speed of travelator.
    :ivar length: Length (integer in meters).+v1.1
    :ivar gradient: Slope (integer in meters) for inclined moving
        walks.+v1.1
    :ivar integrates_an_escalator_part: Whether the moving walk has an
        escalator part. +v1.1
    """
    class Meta:
        name = "TravelatorEquipment_VersionStructure"

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
    speed: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Speed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gradient: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    integrates_an_escalator_part: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IntegratesAnEscalatorPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
