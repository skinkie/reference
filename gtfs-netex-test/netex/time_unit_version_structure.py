from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.fare_unit_version_structure import FareUnitVersionStructure
from netex.time_unit_prices_rel_structure import TimeUnitPricesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeUnitVersionStructure(FareUnitVersionStructure):
    """
    Type for TIME UNIT.

    :ivar type_value: Name of Class associated with uit, e.g. gDay,
        gTime, etc.
    :ivar duration: Duration of Unit, eg   P1D,  P1S, etc.
    :ivar prices: PRICEs of TIME UNIT.
    """
    class Meta:
        name = "TimeUnit_VersionStructure"

    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[TimeUnitPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
