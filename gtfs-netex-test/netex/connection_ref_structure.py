from dataclasses import dataclass
from .transfer_ref_structure import TransferRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionRefStructure(TransferRefStructure):
    value: RestrictedVar
