from dataclasses import dataclass

from .tractive_rolling_stock_item_ref_structure import TractiveRollingStockItemRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TractiveRollingStockItemRef(TractiveRollingStockItemRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
