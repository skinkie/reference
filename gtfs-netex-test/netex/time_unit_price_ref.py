from dataclasses import dataclass
from netex.time_unit_price_ref_structure import TimeUnitPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeUnitPriceRef(TimeUnitPriceRefStructure):
    """
    Reference to a TIME UNIT PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
