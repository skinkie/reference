from dataclasses import dataclass
from netex.transfer_ref_structure import TransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConnectionRefStructure(TransferRefStructure):
    """
    Type for a reference to a CONNECTION link.
    """
