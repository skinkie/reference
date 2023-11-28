from dataclasses import dataclass
from netex.online_service_ref_structure import OnlineServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OnlineServiceRef(OnlineServiceRefStructure):
    """Identifier of an ONLINE SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
