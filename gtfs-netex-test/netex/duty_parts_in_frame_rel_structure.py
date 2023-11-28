from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.duty_part import DutyPart

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyPartsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of DUTY PARTs.
    """
    class Meta:
        name = "dutyPartsInFrame_RelStructure"

    duty_part: List[DutyPart] = field(
        default_factory=list,
        metadata={
            "name": "DutyPart",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
