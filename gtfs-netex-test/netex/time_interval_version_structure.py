from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.fare_interval_version_structure import FareIntervalVersionStructure
from netex.time_interval_prices_rel_structure import TimeIntervalPricesRelStructure
from netex.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeIntervalVersionStructure(FareIntervalVersionStructure):
    """
    Type for TIME INTERVAL.

    :ivar start_time: Start time for TIME INTERVAL if restricted to a
        specific time.
    :ivar end_time: End value for TIME INTERVAL.
    :ivar day_offset: Day Offset for end time from start time. 0= same
        day.
    :ivar duration: MaximumDuration for TIME INTERVAL.
    :ivar minimum_duration: Minimum Duration for TIME INTERVAL. +v1.1
    :ivar prices: PRICEs of TIME INTERVAL.
    :ivar time_structure_factors: TIME STRUCTURE FACTORs associated with
        this element.
    """
    class Meta:
        name = "TimeInterval_VersionStructure"

    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DayOffset",
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
    minimum_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[TimeIntervalPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
