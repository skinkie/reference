from dataclasses import dataclass
from .entitlement_product_ref_structure import EntitlementProductRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementProductRef(EntitlementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
