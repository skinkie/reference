from dataclasses import dataclass
from .management_agent_ref_structure import ManagementAgentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ManagementAgentRef(ManagementAgentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
