from dataclasses import dataclass, field
from netex.vehicle_manoeuvring_requirement_version_structure import VehicleManoeuvringRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleManoeuvringRequirement(VehicleManoeuvringRequirementVersionStructure):
    """
    Requirements for carrying passengers.

    :ivar id: Identifier of VEHICLE MANOEVRING REQUIREMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
