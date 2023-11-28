from dataclasses import dataclass
from netex.default_connection_ref_structure import DefaultConnectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultConnectionRef(DefaultConnectionRefStructure):
    """
    Reference to a DEFAULT TRANSFER link.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
