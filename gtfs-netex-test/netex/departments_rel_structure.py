from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.department import Department
from netex.department_ref import DepartmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DepartmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DEPARTMENTs.
    """
    class Meta:
        name = "departments_RelStructure"

    department_ref_or_department: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DepartmentRef",
                    "type": DepartmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Department",
                    "type": Department,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
