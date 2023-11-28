from dataclasses import dataclass, field
from netex.management_agent_version_structure import ManagementAgentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ManagementAgent(ManagementAgentVersionStructure):
    """
    ORGANISATION that manages data or a SITE or FACILITY.

    :ivar id: Identifier of MANAGEMENT AGENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
