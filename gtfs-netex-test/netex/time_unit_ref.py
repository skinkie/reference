from dataclasses import dataclass
from .time_unit_ref_structure import TimeUnitRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitRef(TimeUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
