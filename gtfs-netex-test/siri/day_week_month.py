from dataclasses import dataclass, field
from typing import List, Optional

from .day_enum import DayEnum
from .extension_type import ExtensionType
from .month_of_year_enum import MonthOfYearEnum
from .week_of_month_enum import WeekOfMonthEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class DayWeekMonth:
    applicable_day: List[DayEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 7,
        },
    )
    applicable_week: List[WeekOfMonthEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableWeek",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 5,
        },
    )
    applicable_month: List[MonthOfYearEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_occurs": 12,
        },
    )
    day_week_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dayWeekMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
