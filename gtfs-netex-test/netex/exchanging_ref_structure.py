from dataclasses import dataclass
from netex.reselling_ref_structure import ResellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExchangingRefStructure(ResellingRefStructure):
    """
    Type for Reference to a EXCHANGING USAGE PARAMETER.
    """
