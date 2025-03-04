from dataclasses import dataclass

from .management_agent_ref_structure import ManagementAgentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ManagementAgentRef(ManagementAgentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
