from dataclasses import dataclass
from netex.network_ref_structure import NetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NetworkRef(NetworkRefStructure):
    """
    Reference to a NETWORK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
