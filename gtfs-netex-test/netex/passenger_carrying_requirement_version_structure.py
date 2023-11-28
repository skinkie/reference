from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.passenger_capacity import PassengerCapacity
from netex.vehicle_requirement_version_structure import VehicleRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCarryingRequirementVersionStructure(VehicleRequirementVersionStructure):
    """
    Type for a PASSENGER CARRYING REQUIREMENT.

    :ivar passenger_capacity:
    :ivar low_floor: Whether Vehicle is low floor to facilitate access
        by the mobility impaired.
    :ivar has_lift_or_ramp: Whether vehicle has lift or ramp to
        facilitate wheelchair access.
    :ivar has_hoist: Whether vehicle has hoist for wheelchair access.
    :ivar boarding_height: Maximum step height to board. +v1.1
    :ivar gap_to_platform: Expected maximal gap between VEHICLE and
        platform. +v1.1
    """
    class Meta:
        name = "PassengerCarryingRequirement_VersionStructure"

    passenger_capacity: Optional[PassengerCapacity] = field(
        default=None,
        metadata={
            "name": "PassengerCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    low_floor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LowFloor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_lift_or_ramp: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasLiftOrRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_hoist: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasHoist",
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
