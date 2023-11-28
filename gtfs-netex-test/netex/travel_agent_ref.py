from dataclasses import dataclass
from netex.travel_agent_ref_structure import TravelAgentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelAgentRef(TravelAgentRefStructure):
    """
    Reference to a TRAVEL AGENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
