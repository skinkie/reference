from dataclasses import dataclass

from .recharging_step_version_structure import RechargingStepVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingStep(RechargingStepVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
