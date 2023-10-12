from dataclasses import dataclass
from netex.day_type_ref_structure import DayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DayTypeRef(DayTypeRefStructure):
    """
    Reference to a DAY TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
