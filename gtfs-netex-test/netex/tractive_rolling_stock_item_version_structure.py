from dataclasses import dataclass, field
from typing import Optional

from .rolling_stock_item_version_structure import RollingStockItemVersionStructure
from .tractive_element_type_ref import TractiveElementTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TractiveRollingStockItemVersionStructure(RollingStockItemVersionStructure):
    class Meta:
        name = "TractiveRollingStockItem_VersionStructure"

    tractive_element_type_ref: Optional[TractiveElementTypeRef] = field(
        default=None,
        metadata={
            "name": "TractiveElementTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
