from dataclasses import dataclass

from .price_unit_version_structure import PriceUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PriceUnit(PriceUnitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
