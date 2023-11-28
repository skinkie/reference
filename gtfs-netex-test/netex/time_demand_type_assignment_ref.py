from dataclasses import dataclass
from netex.time_demand_type_assignment_ref_structure import TimeDemandTypeAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypeAssignmentRef(TimeDemandTypeAssignmentRefStructure):
    """
    Reference to a TIME DEMAND ASSIGNMENT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
