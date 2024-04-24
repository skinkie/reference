from dataclasses import dataclass

from .type_of_rolling_stock_value_structure import TypeOfRollingStockValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRollingStock(TypeOfRollingStockValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
