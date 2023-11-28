from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.duty_part import DutyPart
from netex.duty_part_ref import DutyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyPartsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DUTY PARTs.
    """
    class Meta:
        name = "dutyParts_RelStructure"

    duty_part_ref_or_duty_part: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DutyPartRef",
                    "type": DutyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DutyPart",
                    "type": DutyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
