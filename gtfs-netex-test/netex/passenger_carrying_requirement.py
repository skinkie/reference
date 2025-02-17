from dataclasses import dataclass

from .passenger_carrying_requirement_version_structure import PassengerCarryingRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerCarryingRequirement(PassengerCarryingRequirementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
