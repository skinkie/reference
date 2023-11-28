from dataclasses import dataclass
from netex.refunding_ref_structure import RefundingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RefundingRef(RefundingRefStructure):
    """
    Reference to a REFUNDING USAGE PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
