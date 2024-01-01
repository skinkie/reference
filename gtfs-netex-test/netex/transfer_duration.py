from dataclasses import dataclass
from .transfer_duration_structure import TransferDurationStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferDuration(TransferDurationStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
