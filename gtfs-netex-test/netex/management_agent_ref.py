from dataclasses import dataclass
from netex.management_agent_ref_structure import ManagementAgentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ManagementAgentRef(ManagementAgentRefStructure):
    """
    Reference to a MANAGEMENT AGENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
