from dataclasses import dataclass, field
from typing import List
from netex.check_constraint import CheckConstraint
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CHECK CONSTRAINTs.
    """
    class Meta:
        name = "checkConstraintInFrame_RelStructure"

    check_constraint: List[CheckConstraint] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
