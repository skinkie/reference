from dataclasses import dataclass

from .time_unit_price_ref_structure import TimeUnitPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeUnitPriceRef(TimeUnitPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
