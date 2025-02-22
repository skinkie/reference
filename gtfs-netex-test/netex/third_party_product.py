from dataclasses import dataclass

from .third_party_product_version_structure import ThirdPartyProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ThirdPartyProduct(ThirdPartyProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
