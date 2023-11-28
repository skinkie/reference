from dataclasses import dataclass, field
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.entrance_attention_enumeration import EntranceAttentionEnumeration
from netex.necessary_force_enumeration import NecessaryForceEnumeration
from netex.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntranceEquipmentVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for an ENTRANCE EQUIPMENT.

    :ivar door: Whether there is a door in the entrance. If false,
        opening does not have door.
    :ivar kept_open: Whether the door is kept open.
    :ivar revolving_door: Whether door is revolving. Only applies if
        door is specified.
    :ivar barrier: Whether there is a physical barrier across the
        doorway.
    :ivar number_of_gates: Number of gates in barrier or entrance.
    :ivar staffing: Staffing of entrance or barrier.
    :ivar entrance_requires_staffing: Whether entrance requires staff
        for use.
    :ivar entrance_requires_ticket: Whether passage requires ticket.
    :ivar entrance_requires_passport: Whether passage requires passport.
    :ivar drop_kerb_outside: Whether there is a drop Kerb outside door.
    :ivar acoustic_sensor: Whether door has acoustic sensors.
    :ivar automatic_door: Whether doors are automatic.
    :ivar glass_door: Whether door is made of glass.
    :ivar airlock: Whether there is an airlock. +v1.1
    :ivar wheelchair_passable: Door can be passed in a wheel chair.
    :ivar wheelchair_unaided: Can be passed in a wheel chair unaided.
    :ivar audio_or_video_intercom: Whether there is an audio or video
        communication needed for access. +v1.1
    :ivar entrance_attention: Nature of doorbell help point etc needed
        to operate door.
    :ivar doorstep_mark: Whether there is a tactile doorstep mark. +v1.1
    :ivar necessary_force_to_open: Necessary force to open the door.
        +v1.1
    :ivar suitable_for_cycles: Whether equipment is suitable for cycles.
    :ivar audio_passthrough_indicator: Whether there is an audio signal
        indicating passing through
    :ivar opening_necessary_force: Necessary force to open the door
    """
    class Meta:
        name = "EntranceEquipment_VersionStructure"

    door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Door",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    kept_open: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeptOpen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    revolving_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RevolvingDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    barrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Barrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_gates: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfGates",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    staffing: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_requires_staffing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EntranceRequiresStaffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_requires_ticket: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EntranceRequiresTicket",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_requires_passport: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EntranceRequiresPassport",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    drop_kerb_outside: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DropKerbOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    acoustic_sensor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AcousticSensor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    automatic_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomaticDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    glass_door: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GlassDoor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    airlock: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Airlock",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_passable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairPassable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_unaided: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairUnaided",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_or_video_intercom: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioOrVideoIntercom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    entrance_attention: Optional[EntranceAttentionEnumeration] = field(
        default=None,
        metadata={
            "name": "EntranceAttention",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    doorstep_mark: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DoorstepMark",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    necessary_force_to_open: Optional[NecessaryForceEnumeration] = field(
        default=None,
        metadata={
            "name": "NecessaryForceToOpen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_passthrough_indicator: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioPassthroughIndicator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    opening_necessary_force: Optional[NecessaryForceEnumeration] = field(
        default=None,
        metadata={
            "name": "OpeningNecessaryForce",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
