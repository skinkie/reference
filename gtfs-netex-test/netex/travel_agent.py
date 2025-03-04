from dataclasses import dataclass

from .travel_agent_version_structure import TravelAgentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TravelAgent(TravelAgentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
