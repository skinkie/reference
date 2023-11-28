from dataclasses import dataclass, field
from netex.charging_policy_version_structure import ChargingPolicyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ChargingPolicy(ChargingPolicyVersionStructure):
    """
    Policy regarding different aspects of charging such as credit limits.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
