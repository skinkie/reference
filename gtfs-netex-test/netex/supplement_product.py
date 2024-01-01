from dataclasses import dataclass
from .supplement_product_version_structure import (
    SupplementProductVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SupplementProduct(SupplementProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
