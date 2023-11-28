from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.duty_part_ref import DutyPartRef
from netex.journey_part_ref import JourneyPartRef
from netex.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DeadRunCallPartStructure:
    """
    Type for DEAD RUN CALL part.

    :ivar time: Latest Arrival time.
    :ivar day_offset: Number of days of arrival time after the starting
        day  journey if  not same calendar day. Default is 0 for same
        day.
    :ivar wait_time: Timetabled waiting interval.
    :ivar journey_part_ref:
    :ivar time_demand_type_ref:
    :ivar duty_part_ref:
    """
    time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "Time",
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
    wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "WaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_ref: Optional[JourneyPartRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_part_ref: Optional[DutyPartRef] = field(
        default=None,
        metadata={
            "name": "DutyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
