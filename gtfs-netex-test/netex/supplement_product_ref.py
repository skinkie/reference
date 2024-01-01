from dataclasses import dataclass
from .supplement_product_ref_structure import SupplementProductRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplementProductRef(SupplementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
