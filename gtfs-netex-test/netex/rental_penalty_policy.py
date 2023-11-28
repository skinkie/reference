from dataclasses import dataclass, field
from netex.rental_penalty_policy_version_structure import RentalPenaltyPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalPenaltyPolicy(RentalPenaltyPolicyVersionStructure):
    """
    Policy regarding different aspects of RENTAL service penalty charges, for
    example loss of vehicle.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
