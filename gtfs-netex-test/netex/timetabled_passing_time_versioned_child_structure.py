from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.headway_interval_structure import HeadwayIntervalStructure
from netex.passing_time_versioned_child_structure import PassingTimeVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimetabledPassingTimeVersionedChildStructure(PassingTimeVersionedChildStructure):
    """
    Type for TIMETABLED PASSING TIME.

    :ivar arrival_time: Timetabled arrival time.
    :ivar arrival_day_offset: Number of days after the starting time of
        the journey if  not same calendar day. Default is 0 for same
        day.
    :ivar departure_time: Timetabled departure time.
    :ivar departure_day_offset: Number of days after the starting time
        of the journey if  not same calendar day. Default is 0 for same
        day.
    :ivar waiting_time: Timetabled waiting interval.
    :ivar headway: Frequency of service.
    :ivar latest_arrival_time: Latest Arrival Time.
    :ivar latest_arrival_day_offset: Number of days after the starting
        time of the journey if  not same calendar day. Default is 0 for
        same day.
    :ivar earliest_departure_time: Earliest Timetabled departure time.
    :ivar earliest_departure_day_offset: Number of days after the
        starting time of the journey if  not same calendar day. Default
        is 0 for same day.
    """
    class Meta:
        name = "TimetabledPassingTime_VersionedChildStructure"

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
    latest_arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestArrivalTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    latest_arrival_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "LatestArrivalDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestDepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EarliestDepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
