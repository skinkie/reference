from dataclasses import dataclass
from netex.operating_day_ref_structure import OperatingDayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OperatingDayRef(OperatingDayRefStructure):
    """
    Reference to an OPERATING DAY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
