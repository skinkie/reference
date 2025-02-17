from dataclasses import dataclass

from .priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FulfilmentMethodRefStructure(PriceableObjectRefStructure):
    pass
