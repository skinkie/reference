from dataclasses import dataclass, field

from .month_validity_offset import MonthValidityOffset
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MonthValidityOffsetsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "monthValidityOffsets_RelStructure"

    month_validity_offset: list[MonthValidityOffset] = field(
        default_factory=list,
        metadata={
            "name": "MonthValidityOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
