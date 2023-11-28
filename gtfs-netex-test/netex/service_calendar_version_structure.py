from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlDuration, XmlTime
from netex.alternative_texts_rel_structure import (
    DataManagedObjectStructure,
    DayTypesRelStructure,
    OperatingDaysRelStructure,
    TimebandsRelStructure,
)
from netex.day_type_assignments_rel_structure import DayTypeAssignmentsRelStructure
from netex.multilingual_string import MultilingualString
from netex.operating_periods_rel_structure import OperatingPeriodsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceCalendarVersionStructure(DataManagedObjectStructure):
    """
    Type for a SERVICE CALENDAR.

    :ivar name: Name of SERVIC CALENDAR.
    :ivar short_name: Short Name of SERVIC CALENDAR.
    :ivar from_date: Start date of Calendar.
    :ivar to_date: End date of SERVICE CALENDAR. Date is INCLUSIVE.
    :ivar earliest_time: Earliest time that day starts. Default is 00:00
    :ivar day_length: Length of day. Used to work out latest time that
        day runs to. Default is 24hourse.
    :ivar day_types: Reusable DAY TYPE used in calendar.
    :ivar timebands: Reusable Time bands used in calendar.
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
        name = "ServiceCalendar_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FromDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ToDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    earliest_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EarliestTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_length: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DayLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_types: Optional[DayTypesRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timebands: Optional[TimebandsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_days: Optional[OperatingDaysRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingDays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operating_periods: Optional[OperatingPeriodsRelStructure] = field(
        default=None,
        metadata={
            "name": "operatingPeriods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    day_type_assignments: Optional[DayTypeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
