from dataclasses import dataclass
from .capability_request_policy_structure import (
    CapabilityRequestPolicyStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectCapabilityRequestPolicyStructure(
    CapabilityRequestPolicyStructure
):
    pass
