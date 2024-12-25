from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .recharging_plan import RechargingPlan

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingPlansRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "rechargingPlans_RelStructure"

    recharging_plan: list[RechargingPlan] = field(
        default_factory=list,
        metadata={
            "name": "RechargingPlan",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
