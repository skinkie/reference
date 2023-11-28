from dataclasses import dataclass
from netex.penalty_policy_ref_structure import PenaltyPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PenaltyPolicyRef(PenaltyPolicyRefStructure):
    """
    Reference to a PENALTY POLICY usage parameter.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
