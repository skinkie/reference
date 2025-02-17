from dataclasses import dataclass

from .capability_request_policy_structure import CapabilityRequestPolicyStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataObjectCapabilityRequestPolicyStructure(CapabilityRequestPolicyStructure):
    pass
