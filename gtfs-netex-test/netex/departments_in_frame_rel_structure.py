from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .department import Department

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DepartmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "departmentsInFrame_RelStructure"

    department: list[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
