from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .tractive_rolling_stock_item import TractiveRollingStockItem
from .tractive_rolling_stock_item_ref import TractiveRollingStockItemRef
from .trailing_rolling_stock_item import TrailingRollingStockItem
from .trailing_rolling_stock_item_ref import TrailingRollingStockItemRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockItemsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "rollingStockItems_RelStructure"

    rolling_stock_item_ref_or_rolling_stock_item_dummy_type: List[Union[TrailingRollingStockItemRef, TractiveRollingStockItemRef, TractiveRollingStockItem, TrailingRollingStockItem]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrailingRollingStockItemRef",
                    "type": TrailingRollingStockItemRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveRollingStockItemRef",
                    "type": TractiveRollingStockItemRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TractiveRollingStockItem",
                    "type": TractiveRollingStockItem,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrailingRollingStockItem",
                    "type": TrailingRollingStockItem,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
