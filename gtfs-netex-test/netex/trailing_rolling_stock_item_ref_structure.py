from dataclasses import dataclass

from .rolling_stock_item_ref_structure import RollingStockItemRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TrailingRollingStockItemRefStructure(RollingStockItemRefStructure):
    pass
