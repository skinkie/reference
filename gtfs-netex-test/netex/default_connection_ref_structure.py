from dataclasses import dataclass
from netex.connection_ref_structure import ConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultConnectionRefStructure(ConnectionRefStructure):
    """
    Type for a reference to a DEFAULT TRANSFER link.
    """
