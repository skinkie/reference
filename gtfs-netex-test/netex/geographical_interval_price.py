from dataclasses import dataclass
from .geographical_interval_price_versioned_child_structure import (
    GeographicalIntervalPriceVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalIntervalPrice(
    GeographicalIntervalPriceVersionedChildStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
