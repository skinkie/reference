from dataclasses import dataclass, field
from typing import Optional
from netex.common_version_frame_structure import CommonVersionFrameStructure
from netex.day_type_assignments_in_frame_rel_structure import DayTypeAssignmentsInFrameRelStructure
from netex.day_types_in_frame_rel_structure import DayTypesInFrameRelStructure
from netex.group_of_timebands_in_frame_rel_structure import GroupOfTimebandsInFrameRelStructure
from netex.operating_days_in_frame_rel_structure import OperatingDaysInFrameRelStructure
from netex.operating_periods_in_frame_rel_structure import OperatingPeriodsInFrameRelStructure
from netex.service_calendar import ServiceCalendar
from netex.timebands_in_frame_rel_structure import TimebandsInFrameRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceCalendarFrameVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a SERVICE CALENDAR.

    :ivar service_calendar:
    :ivar day_types: Reusable DAY TYPE  in SERVICE CALENDAR FRAME.
    :ivar timebands: Reusable TIMEBANDs used in SERVICE CALENDAR FRAME.
    :ivar group_of_timebands: GROUPs OF TIMEBANDs   in SERVICE CALENDAR
        FRAME.
    :ivar operating_days: Days found in Calendar between start and end
        date. Dates must fall between the start and end date of the
        calendar.  There is a day for every date in the calendar
        validity period. Days do not have to be explicitly declared if
        there is no additional information.
    :ivar operating_periods: OPERATING PERIODs belonging to calendar.
        Named periods. Must fall within the overall validity period of
        the calendar.
    :ivar day_type_assignments: Assignments of DAY TYPEs to specific
        OPERATING DAYs. The same DAY TYPE may be assigned to multiple
        Operating dates, and vice versa.
    """
    class Meta:
        name = "ServiceCalendarFrame_VersionFrameStructure"

    service_calendar: Optional[ServiceCalendar] = field(
        default=None,
        metadata={
            "name": "ServiceCalendar",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[DayTypesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timebands: Optional[TimebandsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timebands: Optional[GroupOfTimebandsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupOfTimebands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_days: Optional[OperatingDaysInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_periods: Optional[OperatingPeriodsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingPeriods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_assignments: Optional[DayTypeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
