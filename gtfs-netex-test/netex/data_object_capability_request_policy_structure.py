from dataclasses import dataclass
from netex.capability_request_policy_structure import CapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    """
    Type for Monitoring Service Capability Request Policy.
    """
