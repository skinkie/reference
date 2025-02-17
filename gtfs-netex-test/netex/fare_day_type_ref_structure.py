from dataclasses import dataclass

from .day_type_ref_structure import DayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareDayTypeRefStructure(DayTypeRefStructure):
    pass
