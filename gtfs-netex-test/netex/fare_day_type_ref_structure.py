from dataclasses import dataclass
from .day_type_ref_structure import DayTypeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareDayTypeRefStructure(DayTypeRefStructure):
    value: RestrictedVar
