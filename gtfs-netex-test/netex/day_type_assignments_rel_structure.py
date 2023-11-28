from dataclasses import dataclass, field
from typing import List
from netex.day_type_assignment import DayTypeAssignment
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DayTypeAssignmentsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of  DAY TYPE ASSIGNMENT.

    :ivar day_type_assignment: An operating period.
    """
    class Meta:
        name = "dayTypeAssignments_RelStructure"

    day_type_assignment: List[DayTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "DayTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
