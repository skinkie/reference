from dataclasses import dataclass, field
from netex.penalty_policy_version_structure import PenaltyPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PenaltyPolicy(PenaltyPolicyVersionStructure):
    """
    Policy regarding different aspects of penalty charges, for example  repeated
    entry at the same station, no ticket etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
