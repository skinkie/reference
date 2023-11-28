from dataclasses import dataclass, field
from typing import List
from netex.day_of_week_enumeration import DayOfWeekEnumeration
from netex.operating_period_version_structure import OperatingPeriodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicOperatingPeriodVersionStructure(OperatingPeriodVersionStructure):
    """
    Type for an OPERATING DAY.

    :ivar valid_day_bits: String of bits, one for each day in period:
        whether valid or not valid on the day.  Normally there will be a
        bit for every day between start and end date.  If bit is
        missing, assume available.
    :ivar days_of_week: Days of week to which bits correspond.
    """
    class Meta:
        name = "UicOperatingPeriod_VersionStructure"

    valid_day_bits: str = field(
        metadata={
            "name": "ValidDayBits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
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
