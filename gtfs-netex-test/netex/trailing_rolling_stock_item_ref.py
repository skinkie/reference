from dataclasses import dataclass

from .trailing_rolling_stock_item_ref_structure import TrailingRollingStockItemRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrailingRollingStockItemRef(TrailingRollingStockItemRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
