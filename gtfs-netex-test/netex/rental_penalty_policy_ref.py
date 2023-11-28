from dataclasses import dataclass
from netex.rental_penalty_policy_ref_structure import RentalPenaltyPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalPenaltyPolicyRef(RentalPenaltyPolicyRefStructure):
    """Reference to a RENTAL PENALTY POLICY usage parameter.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
