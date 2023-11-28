from dataclasses import dataclass
from netex.exchanging_ref_structure import ExchangingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExchangingRef(ExchangingRefStructure):
    """
    Reference to a EXCHANGING USAGE PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
