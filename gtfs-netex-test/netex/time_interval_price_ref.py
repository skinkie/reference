from dataclasses import dataclass

from .time_interval_price_ref_structure import TimeIntervalPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeIntervalPriceRef(TimeIntervalPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
