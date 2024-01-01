from dataclasses import dataclass
from .third_party_product_ref_structure import ThirdPartyProductRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ThirdPartyProductRef(ThirdPartyProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
