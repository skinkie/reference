from dataclasses import dataclass
from netex.time_demand_type_ref_structure import TimeDemandTypeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypeRef(TimeDemandTypeRefStructure):
    """Reference to a TIME DEMAND TYPE.

    If given by context need not be stated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
