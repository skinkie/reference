from dataclasses import dataclass

from .preassigned_fare_product_version_structure import PreassignedFareProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PreassignedFareProduct(PreassignedFareProductVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
