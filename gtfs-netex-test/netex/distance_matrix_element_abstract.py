from dataclasses import dataclass

from .priceable_object_version_structure import PriceableObjectVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementAbstract(PriceableObjectVersionStructure):
    class Meta:
        name = "DistanceMatrixElement_"
        namespace = "http://www.netex.org.uk/netex"
