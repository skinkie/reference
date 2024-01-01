from dataclasses import dataclass
from .geographical_interval_price_ref_structure import (
    GeographicalIntervalPriceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalIntervalPriceRef(GeographicalIntervalPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
