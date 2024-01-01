from dataclasses import dataclass
from .price_unit_ref_structure import PriceUnitRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnitRef(PriceUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
