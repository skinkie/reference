from dataclasses import dataclass
from netex.day_type_ref_structure import DayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareDayTypeRefStructure(DayTypeRefStructure):
    """
    Type for Reference to a FARE DAY TYPE.
    """
    value: RestrictedVar
