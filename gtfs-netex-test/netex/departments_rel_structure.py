from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .department import Department
from .department_ref import DepartmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DepartmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "departments_RelStructure"

    department_ref_or_department: list[Union[DepartmentRef, Department]] = field(
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
        },
    )
