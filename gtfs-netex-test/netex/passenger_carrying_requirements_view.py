from dataclasses import dataclass
from netex.passenger_carrying_requirement_version_structure import PassengerCarryingRequirementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCarryingRequirementsView(PassengerCarryingRequirementVersionStructure):
    """
    Requirements for carrying passengers.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
