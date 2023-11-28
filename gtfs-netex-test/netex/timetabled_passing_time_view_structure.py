from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.headway_interval_structure import HeadwayIntervalStructure
from netex.passing_time_view_structure import PassingTimeViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetabledPassingTimeViewStructure(PassingTimeViewStructure):
    """
    Type for Simplified  TIMETABLED PASSING TIME.

    :ivar arrival_time: Timetabled Arrival time.
    :ivar arrival_day_offset: Arrival Day Offset from Start of Journey.
    :ivar departure_time: Timetabled departure time.
    :ivar departure_day_offset: Number of days after the starting
        departure time of the journey if  not same calendar day. Default
        is 0 for same day.
    :ivar waiting_time: Timetabled waiting interval.
    :ivar headway: Frequency of service.
    """
    class Meta:
        name = "TimetabledPassingTime_ViewStructure"

    arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "ArrivalDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    waiting_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway: Optional[HeadwayIntervalStructure] = field(
        default=None,
        metadata={
            "name": "Headway",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
