from dataclasses import dataclass

from .trailing_rolling_stock_item_version_structure import TrailingRollingStockItemVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrailingRollingStockItem(TrailingRollingStockItemVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
