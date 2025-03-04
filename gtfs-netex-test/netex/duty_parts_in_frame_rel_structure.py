from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .duty_part import DutyPart

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DutyPartsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "dutyPartsInFrame_RelStructure"

    duty_part: list[DutyPart] = field(
        default_factory=list,
        metadata={
            "name": "DutyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
