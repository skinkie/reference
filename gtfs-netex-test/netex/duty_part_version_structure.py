from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.accountable_element_structure import AccountableElementStructure
from netex.duty_ref import DutyRef
from netex.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyPartVersionStructure(AccountableElementStructure):
    """
    Type for a DUTY PART.

    :ivar driver_access_duration: Time for DRIVER to access DUTY PART.
    :ivar driver_return_duration: Time for DRIVER to return from DUTY
        PART.
    :ivar duty_ref:
    :ivar start_time: Start time.
    :ivar day_offset: Day offset for start time. Number of days after
        the current operating day for Duty y . Default is 0 for same
        day.
    :ivar end_time: End time.
    :ivar end_day_offset: Day offset for end time. Number of days after
        the starting departure time of the journey if  not same calendar
        day as starting timey. Default is 0 for same day.
    :ivar start_point_ref: TIMING POINT at which DUTY PART starts.
    :ivar end_point_ref: TIMING POINT at which DUTY PART starts.
    """
    class Meta:
        name = "DutyPart_VersionStructure"

    driver_access_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DriverAccessDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_return_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DriverReturnDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duty_ref: Optional[DutyRef] = field(
        default=None,
        metadata={
            "name": "DutyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
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
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
