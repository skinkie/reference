from dataclasses import dataclass
from .fare_structure_element_price_versioned_child_structure import (
    FareStructureElementPriceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementPrice(
    FareStructureElementPriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions: RestrictedVar
    valid_between: RestrictedVar
    alternative_texts: RestrictedVar
