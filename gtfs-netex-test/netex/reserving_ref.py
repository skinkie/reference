from dataclasses import dataclass
from netex.reserving_ref_structure import ReservingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ReservingRef(ReservingRefStructure):
    """
    Reference to a RESERVING USAGE PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
