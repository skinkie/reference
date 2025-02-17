from dataclasses import dataclass, field

from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .rolling_stock_inventory_ref import RollingStockInventoryRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RollingStockInventoryRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "rollingStockInventoryRefs_RelStructure"

    rolling_stock_inventory_ref: list[RollingStockInventoryRef] = field(
        default_factory=list,
        metadata={
            "name": "RollingStockInventoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
