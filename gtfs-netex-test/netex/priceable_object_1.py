from dataclasses import dataclass

from .priceable_object_version_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PriceableObject1(PriceableObjectVersionStructure):
    class Meta:
        name = "PriceableObject"
        namespace = "http://www.netex.org.uk/netex"
