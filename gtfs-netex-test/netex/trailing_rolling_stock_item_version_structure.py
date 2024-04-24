from dataclasses import dataclass, field
from typing import Optional

from .rolling_stock_item_version_structure import RollingStockItemVersionStructure
from .trailing_element_type_ref import TrailingElementTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrailingRollingStockItemVersionStructure(RollingStockItemVersionStructure):
    class Meta:
        name = "TrailingRollingStockItem_VersionStructure"

    trailing_element_type_ref: Optional[TrailingElementTypeRef] = field(
        default=None,
        metadata={
            "name": "TrailingElementTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
