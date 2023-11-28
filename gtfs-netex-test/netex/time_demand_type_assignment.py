from dataclasses import dataclass, field
from netex.time_demand_type_assignment_version_structure import TimeDemandTypeAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypeAssignment(TimeDemandTypeAssignmentVersionStructure):
    """
    The assignment of a TIME DEMAND TYPE to a TIME BAND depending on the DAY TYPE
    and GROUP OF TIMING LINKS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
