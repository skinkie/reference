from dataclasses import dataclass

from .geographical_interval_price_ref_structure import GeographicalIntervalPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GeographicalIntervalPriceRef(GeographicalIntervalPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
