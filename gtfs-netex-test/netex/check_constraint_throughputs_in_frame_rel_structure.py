from dataclasses import dataclass, field
from typing import List
from netex.check_constraint_delay import CheckConstraintDelay
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintThroughputsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CHECK CONSTRAINT DELAYs.
    """
    class Meta:
        name = "checkConstraintThroughputsInFrame_RelStructure"

    check_constraint_delay: List[CheckConstraintDelay] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
