from dataclasses import dataclass, field

from .recharging_step import RechargingStep
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingStepsRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "rechargingSteps_RelStructure"

    recharging_step: list[RechargingStep] = field(
        default_factory=list,
        metadata={
            "name": "RechargingStep",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
