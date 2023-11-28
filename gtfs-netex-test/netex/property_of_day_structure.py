from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlPeriod
from netex.country_ref_structure import CountryRefStructure
from netex.crowding_enumeration import CrowdingEnumeration
from netex.day_event_enumeration import DayEventEnumeration
from netex.day_of_week_enumeration import DayOfWeekEnumeration
from netex.holiday_type_enumeration import HolidayTypeEnumeration
from netex.multilingual_string import MultilingualString
from netex.season_enumeration import SeasonEnumeration
from netex.tide_enumeration import TideEnumeration
from netex.week_of_month_enumeration import WeekOfMonthEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PropertyOfDayStructure:
    """
    Type for Property of Day.

    :ivar name: Name of PROPERTY OF DAY.
    :ivar description: Description of PROPERTY OF DAY.
    :ivar days_of_week: Days of week Monday to Sunday, Everyday. Up to
        seven allowed. Default is Everyday.
    :ivar weeks_of_month: Week of Month. (Default is EveryWeek)
    :ivar month_of_year_or_day_of_month_or_day_of_year:
    :ivar country_ref: Reference to COUNTRY for Holiday.
    :ivar holiday_types: Type of holiday. Default is Any day.
    :ivar seasons: Seasons (Default is Perennially)
    :ivar tides: Tides. Default is All Tides.
    :ivar day_event: Events happening on day.
    :ivar crowding: Relative busyness of day.
    """
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    days_of_week: List[DayOfWeekEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DaysOfWeek",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    weeks_of_month: List[WeekOfMonthEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "WeeksOfMonth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    month_of_year_or_day_of_month_or_day_of_year: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MonthOfYear",
                    "type": XmlPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOfMonth",
                    "type": XmlPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayOfYear",
                    "type": XmlPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    country_ref: Optional[CountryRefStructure] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    holiday_types: List[HolidayTypeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "HolidayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    seasons: List[SeasonEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Seasons",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    tides: List[TideEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "Tides",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    day_event: Optional[DayEventEnumeration] = field(
        default=None,
        metadata={
            "name": "DayEvent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    crowding: Optional[CrowdingEnumeration] = field(
        default=None,
        metadata={
            "name": "Crowding",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
