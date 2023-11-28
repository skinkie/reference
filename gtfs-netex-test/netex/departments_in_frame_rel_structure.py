from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.department import Department

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DepartmentsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DEPARTMENTs.
    """
    class Meta:
        name = "departmentsInFrame_RelStructure"

    department: List[Department] = field(
        default_factory=list,
        metadata={
            "name": "Department",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
