from dataclasses import dataclass
from netex.fare_day_type_ref_structure import FareDayTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareDayTypeRef(FareDayTypeRefStructure):
    """
    Reference to a FARE DAY TYPE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
