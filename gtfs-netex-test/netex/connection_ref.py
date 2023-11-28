from dataclasses import dataclass
from netex.connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConnectionRef(ConnectionRefStructure):
    """
    Reference to a CONNECTION link.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
