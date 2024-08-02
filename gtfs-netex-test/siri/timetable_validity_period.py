from dataclasses import dataclass

from .closed_timestamp_range_structure import ClosedTimestampRangeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TimetableValidityPeriod(ClosedTimestampRangeStructure):
    pass
