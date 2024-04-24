from dataclasses import dataclass, field
from typing import Optional, Union

from .authority_ref import AuthorityRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .operator_ref import OperatorRef
from .rolling_stock_items_rel_structure import RollingStockItemsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockInventoryVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "RollingStockInventory_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_organisation_ref: Optional[Union[AuthorityRef, OperatorRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    rolling_stock_items: Optional[RollingStockItemsRelStructure] = field(
        default=None,
        metadata={
            "name": "rollingStockItems",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
