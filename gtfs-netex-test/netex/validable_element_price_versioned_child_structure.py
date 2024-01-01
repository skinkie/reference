from dataclasses import dataclass, field
from typing import Optional
from .fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from .validable_element_ref import ValidableElementRef


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    class Meta:
        name = "ValidableElementPrice_VersionedChildStructure"

    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
