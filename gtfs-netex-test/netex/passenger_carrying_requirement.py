from dataclasses import dataclass, field
from netex.passenger_carrying_requirement_version_structure import PassengerCarryingRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCarryingRequirement(PassengerCarryingRequirementVersionStructure):
    """
    Requirements for carrying passengers on a service.

    :ivar id: Identifier of PASSENGER CARRYING REQUIREMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
