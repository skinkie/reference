from dataclasses import dataclass
from netex.mobility_service_ref_structure import MobilityServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceRefStructure(MobilityServiceRefStructure):
    """
    Type for a reference to an ONLINE SERVICE.
    """
