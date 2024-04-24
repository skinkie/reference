from dataclasses import dataclass

from .rolling_stock_inventory_ref_structure import RollingStockInventoryRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockInventoryRef(RollingStockInventoryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
