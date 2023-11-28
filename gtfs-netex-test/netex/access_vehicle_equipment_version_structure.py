from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.actual_vehicle_equipment_version_structure import ActualVehicleEquipmentVersionStructure
from netex.assistance_needed_enumeration import AssistanceNeededEnumeration
from netex.assisted_boarding_location_enumeration import AssistedBoardingLocationEnumeration
from netex.mobility_enumeration import MobilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessVehicleEquipmentVersionStructure(ActualVehicleEquipmentVersionStructure):
    """
    Type for an ACCESS VEHICLE EQUIPMENT.

    :ivar low_floor: Low floor VEHICLES can use stop and be accessible.
    :ivar high_floor: High floor VEHICLES can use stop.
    :ivar hoist: VEHICLE Hoist can be used at VEHICLE has a hoist or
        lift  for wheelchairs.
    :ivar hoist_operating_radius: Distance from VEHICLE needed to
        operate hoist.
    :ivar ramp: Whether  a ramp may be used to access VEHICLE.
    :ivar ramp_bearing_capacity: Maximum weight that ramp can bear.
    :ivar number_of_steps: Number of steps to board or alight from
        VEHICLE.
    :ivar boarding_height: Maximum step height to board.
    :ivar gap_to_platform: Normal gap between VEHICLE and platform.
    :ivar width_of_access_area: Width of access area.
    :ivar height_of_access_area: Height of access area.
    :ivar automatic_doors: Whether there are automatic doors.
    :ivar suitable_for: Mobility needs for which access is suitable.
    :ivar assistance_needed: Nature of assistance needed to board -
        level Access allows self-boarding.
    :ivar assisted_boarding_location: Whether special position on
        platform  is needed for boarding.
    :ivar guide_dogs_allowed: Whether a Guide Dog is allowed.
    """
    class Meta:
        name = "AccessVehicleEquipment_VersionStructure"

    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    high_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HighFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hoist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    hoist_operating_radius: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HoistOperatingRadius",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Ramp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ramp_bearing_capacity: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RampBearingCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    boarding_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "BoardingHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gap_to_platform: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "GapToPlatform",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    width_of_access_area: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WidthOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    height_of_access_area: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HeightOfAccessArea",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    automatic_doors: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutomaticDoors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitable_for: List[MobilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SuitableFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    assistance_needed: Optional[AssistanceNeededEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistanceNeeded",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    assisted_boarding_location: Optional[AssistedBoardingLocationEnumeration] = field(
        default=None,
        metadata={
            "name": "AssistedBoardingLocation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    guide_dogs_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GuideDogsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
