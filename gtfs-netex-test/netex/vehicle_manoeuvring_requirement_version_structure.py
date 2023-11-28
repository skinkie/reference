from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.vehicle_requirement_version_structure import VehicleRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleManoeuvringRequirementVersionStructure(VehicleRequirementVersionStructure):
    """
    Type for a VEHICLE Manoeuvring REQUIREMENT.

    :ivar reversible: Whether vehicle must be reversible.
    :ivar minimum_turning_circle: Minimum distance needed to turn
        vehicle.
    :ivar minimum_overtaking_width: Minimum distance needed to overtake.
    :ivar minimum_length: Minimum distance needed to accommodate
        vehicle.
    """
    class Meta:
        name = "VehicleManoeuvringRequirement_VersionStructure"

    reversible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reversible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_overtaking_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumOvertakingWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
