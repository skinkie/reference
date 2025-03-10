from dataclasses import dataclass

from .fare_product_version_structure import FareProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareProduct1(FareProductVersionStructure):
    class Meta:
        name = "FareProduct"
        namespace = "http://www.netex.org.uk/netex"
