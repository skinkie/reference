from dataclasses import dataclass
from .time_unit_price_ref_structure import TimeUnitPriceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitPriceRef(TimeUnitPriceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
