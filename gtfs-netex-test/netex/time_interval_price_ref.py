from dataclasses import dataclass
from netex.time_interval_price_ref_structure import TimeIntervalPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeIntervalPriceRef(TimeIntervalPriceRefStructure):
    """
    Reference to a TIME INTERVAL PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
