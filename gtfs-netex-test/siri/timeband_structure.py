from dataclasses import dataclass

from .half_open_time_range_structure_1 import HalfOpenTimeRangeStructure1

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class TimebandStructure(HalfOpenTimeRangeStructure1):
    pass
