from dataclasses import dataclass

from .supplement_product_version_structure import SupplementProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SupplementProduct(SupplementProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
