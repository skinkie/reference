from dataclasses import dataclass, field
from typing import Optional
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.group_of_timing_links_ref import GroupOfTimingLinksRef
from netex.time_demand_type_ref import TimeDemandTypeRef
from netex.timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypeAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for TIME DEMAND TYPE ASSIGNMENT.
    """
    class Meta:
        name = "TimeDemandTypeAssignment_VersionStructure"

    time_demand_type_ref: Optional[TimeDemandTypeRef] = field(
        default=None,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timeband_ref: Optional[TimebandRef] = field(
        default=None,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_timing_links_ref: Optional[GroupOfTimingLinksRef] = field(
        default=None,
        metadata={
            "name": "GroupOfTimingLinksRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
