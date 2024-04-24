from dataclasses import dataclass

from .type_of_rolling_stock_ref_structure import TypeOfRollingStockRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRollingStockRef(TypeOfRollingStockRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
