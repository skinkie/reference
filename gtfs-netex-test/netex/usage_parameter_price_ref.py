from dataclasses import dataclass
from netex.usage_parameter_price_ref_structure import UsageParameterPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UsageParameterPriceRef(UsageParameterPriceRefStructure):
    """
    Reference to a USAGE PARAMETER PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
