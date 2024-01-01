from dataclasses import dataclass
from .priceable_object_ref_structure import PriceableObjectRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareUnitRefStructure(PriceableObjectRefStructure):
    value: RestrictedVar
