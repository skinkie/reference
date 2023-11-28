from dataclasses import dataclass
from netex.third_party_product_ref_structure import ThirdPartyProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ThirdPartyProductRef(ThirdPartyProductRefStructure):
    """
    Reference to a THIRD PARTY PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
