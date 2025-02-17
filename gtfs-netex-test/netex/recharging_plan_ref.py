from dataclasses import dataclass

from .recharging_plan_ref_structure import RechargingPlanRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RechargingPlanRef(RechargingPlanRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
