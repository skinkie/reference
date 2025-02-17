from dataclasses import dataclass

from .transfer_ref_structure import TransferRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ConnectionRefStructure(TransferRefStructure):
    pass
