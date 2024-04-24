from dataclasses import dataclass, field
from typing import List, Union

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .tractive_rolling_stock_item_ref import TractiveRollingStockItemRef
from .trailing_rolling_stock_item_ref import TrailingRollingStockItemRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockItemRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "rollingStockItemRefs_RelStructure"

    rolling_stock_item_ref: List[Union[TrailingRollingStockItemRef, TractiveRollingStockItemRef]] = field(
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
            ),
        },
    )
