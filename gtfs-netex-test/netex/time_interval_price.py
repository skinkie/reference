from dataclasses import dataclass

from .time_interval_price_versioned_child_structure import TimeIntervalPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeIntervalPrice(TimeIntervalPriceVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
