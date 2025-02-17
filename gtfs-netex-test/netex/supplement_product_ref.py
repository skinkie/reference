from dataclasses import dataclass

from .supplement_product_ref_structure import SupplementProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SupplementProductRef(SupplementProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
