from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from .extension_type import ExtensionType
from .time_period_of_day import TimePeriodOfDay

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TimePeriodByHour(TimePeriodOfDay):
    start_time_of_period: XmlTime = field(
        metadata={
            "name": "startTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    end_time_of_period: XmlTime = field(
        metadata={
            "name": "endTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    time_period_by_hour_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "timePeriodByHourExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
