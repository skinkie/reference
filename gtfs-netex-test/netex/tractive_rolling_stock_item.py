from dataclasses import dataclass

from .tractive_rolling_stock_item_version_structure import TractiveRollingStockItemVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TractiveRollingStockItem(TractiveRollingStockItemVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
