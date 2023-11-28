from dataclasses import dataclass, field
from typing import List
from netex.alternative_texts_rel_structure import (
    AvailabilityCondition,
    ValidBetween,
    ValidDuring,
)
from netex.availability_condition_ref import AvailabilityConditionRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AvailabilityConditionsRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more AVAILABILITY CONDITIONs.
    """
    class Meta:
        name = "availabilityConditions_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": ValidBetween,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
