from dataclasses import dataclass
from netex.transfer_duration_structure import TransferDurationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferDuration(TransferDurationStructure):
    """
    Times for TRANSFER between two Points.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
