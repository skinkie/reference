from dataclasses import dataclass
from .price_group_ref_structure import PriceGroupRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceGroupRef(PriceGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
