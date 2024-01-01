from dataclasses import dataclass
from .access_right_in_product_ref_structure import (
    AccessRightInProductRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightInProductRef(AccessRightInProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
