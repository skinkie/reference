from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.handrail_enumeration import HandrailEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LiftEquipmentVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for a LIFT EQUIPMENT.

    :ivar depth: Depth of lift.
    :ivar maximum_load: Maximum load in Kilos.
    :ivar wheelchair_passable: Whether lift is judged wheelchair
        passable.
    :ivar wheelchair_turning_circle: Turning circle within Lift for a
        wheelchair.
    :ivar internal_width: Internal width of lift.
    :ivar handrail_type: Type of handrail.
    :ivar handrail_height: Height of handrail from floor.
    :ivar lower_handrail_height: Height of lower handrail from floor.
    :ivar call_button_height: Height of call button from ground.
    :ivar direction_button_height: Height of direction call button from
        ground.
    :ivar raised_buttons: Whether buttons are raised.
    :ivar braille_buttons: Whether buttons have braille.
    :ivar tactile_ground_floor_button: Indicates whether there is a
        tactile marker on the go to ground  floor button. +v1.1
    :ivar ground_mark_aligned_with_button: Indicates a tactile marker on
        floor under the buttons (or aligned with) +v1.1 .
    :ivar through_loader: Whether lift is a through loader.
    :ivar mirror_on_opposite_side: Whether Lift has a mirror on opposite
        side.
    :ivar attendant: Whether Lift has an attendant.
    :ivar automatic: Whether lift is automatic.
    :ivar external_floor_selection: Whether the floor selection is made
        outside the lift.+v1.1
    :ivar alarm_button: Whether lift has alarm button.
    :ivar tactile_actuators: Whether Lift has a tactile actuator.
    :ivar audio_announcements: Whether Lift has AudioAnnouncements.
    :ivar accoustic_announcements: DEPRECATED - Spelling correction
        renamed to audio announcements. THis value will be dropped at  -
        so
    :ivar magnetic_induction_loop: Indicates existence of a Magnetic
        Induction Loop. +v1.1
    :ivar signage_to_lift: Whether Lift has good signage to find it.
    :ivar suitable_for_cycles: Whether equipment is suitable for cycles.
    :ivar buttons_height: Indicates buttons height (in centimeter)
    :ivar netex_org_uk_netex_ground_markaligned_with_button: Indicates a
        tactile marker on floor under the buttons (or aligned with).
    """
    class Meta:
        name = "LiftEquipment_VersionStructure"

    depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_load: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MaximumLoad",
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
    wheelchair_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    internal_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "InternalWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    handrail_type: Optional[HandrailEnumeration] = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lower_handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LowerHandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    call_button_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "CallButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_button_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "DirectionButtonHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    raised_buttons: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RaisedButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    braille_buttons: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BrailleButtons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_ground_floor_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGroundFloorButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ground_mark_aligned_with_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GroundMarkAlignedWithButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    through_loader: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ThroughLoader",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mirror_on_opposite_side: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MirrorOnOppositeSide",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    attendant: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Attendant",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    automatic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Automatic",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    external_floor_selection: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ExternalFloorSelection",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alarm_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlarmButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_actuators: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileActuators",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    audio_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AudioAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accoustic_announcements: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccousticAnnouncements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    magnetic_induction_loop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MagneticInductionLoop",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    signage_to_lift: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SignageToLift",
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
    buttons_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "ButtonsHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_ground_markaligned_with_button: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GroundMarkalignedWithButton",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
