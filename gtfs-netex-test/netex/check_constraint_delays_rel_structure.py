from dataclasses import dataclass, field
from typing import List
from netex.check_constraint_delay import CheckConstraintDelay
from netex.check_constraint_delay_ref import CheckConstraintDelayRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintDelaysRelStructure(StrictContainmentAggregationStructure):
    """
    A collection of one or more CHECK CONSTRAINTs.
    """
    class Meta:
        name = "checkConstraintDelays_RelStructure"

    check_constraint_delay_ref_or_check_constraint_delay: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CheckConstraintDelayRef",
                    "type": CheckConstraintDelayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CheckConstraintDelay",
                    "type": CheckConstraintDelay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
