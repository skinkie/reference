from dataclasses import dataclass
from netex.time_unit_ref_structure import TimeUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeUnitRef(TimeUnitRefStructure):
    """
    Reference to a TIME UNIT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
