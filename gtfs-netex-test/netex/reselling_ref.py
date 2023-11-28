from dataclasses import dataclass
from netex.reselling_ref_structure import ResellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResellingRef(ResellingRefStructure):
    """
    Reference to a RESELLING USAGE PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
