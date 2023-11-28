from dataclasses import dataclass
from netex.geographical_interval_price_ref_structure import GeographicalIntervalPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalPriceRef(GeographicalIntervalPriceRefStructure):
    """
    Reference to a GEOGRAPHICAL INTERVAL PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
