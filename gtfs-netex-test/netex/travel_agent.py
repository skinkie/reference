from dataclasses import dataclass, field
from netex.travel_agent_version_structure import TravelAgentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelAgent(TravelAgentVersionStructure):
    """
    A travel agent who can retail travel products.

    :ivar id: Identifier of TRAVEL AGENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
