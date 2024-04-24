from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .rolling_stock_inventory import RollingStockInventory

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockInventoriesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "rollingStockInventories_RelStructure"

    rolling_stock_inventory: RollingStockInventory = field(
        metadata={
            "name": "RollingStockInventory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
