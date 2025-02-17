from dataclasses import dataclass, field

from .check_constraint_delay import CheckConstraintDelay
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CheckConstraintDelaysInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "checkConstraintDelaysInFrame_RelStructure"

    check_constraint_delay: list[CheckConstraintDelay] = field(
        default_factory=list,
        metadata={
            "name": "CheckConstraintDelay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
