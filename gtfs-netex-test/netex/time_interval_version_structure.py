from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration, XmlTime

from .fare_interval_version_structure import FareIntervalVersionStructure
from .time_interval_prices_rel_structure import TimeIntervalPricesRelStructure
from .time_structure_factors_rel_structure import TimeStructureFactorsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeIntervalVersionStructure(FareIntervalVersionStructure):
    class Meta:
        name = "TimeInterval_VersionStructure"

    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[TimeIntervalPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
