from dataclasses import dataclass

from .preassigned_fare_product_ref_structure import PreassignedFareProductRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PreassignedFareProductRef(PreassignedFareProductRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
