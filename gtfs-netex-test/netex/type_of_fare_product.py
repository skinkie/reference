from dataclasses import dataclass

from .type_of_fare_product_version_structure import TypeOfFareProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareProduct(TypeOfFareProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
