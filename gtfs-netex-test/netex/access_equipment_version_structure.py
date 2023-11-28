from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.direction_of_use_enumeration import DirectionOfUseEnumeration
from netex.place_equipment_version_structure import PlaceEquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessEquipmentVersionStructure(PlaceEquipmentVersionStructure):
    """
    Type for an ACCESS EQUIPMENT.

    :ivar width: Width of EQUIPMENT or entrance to EQUIPMENT (e.g.
        Lift).
    :ivar direction_of_use: Direction in which EQUIPMENT. can be used.
        Default is both.
    :ivar passengers_per_minute: Number of passengers per minute that
        can use EQUIPMENT.
    :ivar relative_weighting: Relative weighting to be given to this
        item of EQUIPMENT.
    :ivar safe_for_guide_dog: Whether the access is safe for a guide
        dog. +v1.1
    """
    class Meta:
        name = "AccessEquipment_VersionStructure"

    width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    direction_of_use: Optional[DirectionOfUseEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionOfUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passengers_per_minute: Optional[int] = field(
        default=None,
        metadata={
            "name": "PassengersPerMinute",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relative_weighting: Optional[int] = field(
        default=None,
        metadata={
            "name": "RelativeWeighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    safe_for_guide_dog: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SafeForGuideDog",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
