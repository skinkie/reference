from dataclasses import dataclass

from .rolling_stock_inventory_version_structure import RollingStockInventoryVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockInventory(RollingStockInventoryVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
