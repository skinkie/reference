from dataclasses import dataclass, field
from typing import List, Union

from .availability_condition_ref import AvailabilityConditionRef
from .containment_aggregation_structure import ContainmentAggregationStructure
from .entity_in_version_structure import (
    AvailabilityCondition,
    ValidBetween,
    ValidDuring,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AvailabilityConditionsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "availabilityConditions_RelStructure"

    availability_condition_ref_or_availability_condition_or_valid_during_or_valid_between: List[Union[AvailabilityConditionRef, AvailabilityCondition, ValidDuring, ValidBetween]] = field(
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
        },
    )
