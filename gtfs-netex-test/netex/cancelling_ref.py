from dataclasses import dataclass
from netex.cancelling_ref_structure import CancellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CancellingRef(CancellingRefStructure):
    """
    Reference to a CANCELLING PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
