from dataclasses import dataclass

from .recharging_plan_version_structure import RechargingPlanVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RechargingPlan(RechargingPlanVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
