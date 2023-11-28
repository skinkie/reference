from dataclasses import dataclass
from netex.suspending_ref_structure import SuspendingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SuspendingRef(SuspendingRefStructure):
    """
    Reference to a SUSPENDING.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
