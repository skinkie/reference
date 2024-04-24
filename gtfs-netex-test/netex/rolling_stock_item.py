from dataclasses import dataclass

from .rolling_stock_item_version_structure import RollingStockItemVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockItem(RollingStockItemVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
