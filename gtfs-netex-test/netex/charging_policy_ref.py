from dataclasses import dataclass

from .charging_policy_ref_structure import ChargingPolicyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ChargingPolicyRef(ChargingPolicyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
