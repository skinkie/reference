from dataclasses import dataclass
from netex.passenger_carrying_requirement_ref_structure import PassengerCarryingRequirementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCarryingRequirementRef(PassengerCarryingRequirementRefStructure):
    """
    Reference to a PASSENGER CARRYING REQUIREMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
