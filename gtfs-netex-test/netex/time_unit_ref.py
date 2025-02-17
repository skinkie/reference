from dataclasses import dataclass

from .time_unit_ref_structure import TimeUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimeUnitRef(TimeUnitRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
