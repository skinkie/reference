from dataclasses import dataclass

from .recharging_step_ref_structure import RechargingStepRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RechargingStepRef(RechargingStepRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
