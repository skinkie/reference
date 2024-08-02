from dataclasses import dataclass, field
from typing import List

from .days_of_week_enumerationx import DaysOfWeekEnumerationx
from .half_open_time_range_structure_2 import HalfOpenTimeRangeStructure2
from .half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from .holiday_type_enumerationx import HolidayTypeEnumerationx

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoringValidityConditionStructure:
    period: List[HalfOpenTimestampOutputRangeStructure] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timeband: List[HalfOpenTimeRangeStructure2] = field(
        default_factory=list,
        metadata={
            "name": "Timeband",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    day_type: List[DaysOfWeekEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "DayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    holiday_type: List[HolidayTypeEnumerationx] = field(
        default_factory=list,
        metadata={
            "name": "HolidayType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
