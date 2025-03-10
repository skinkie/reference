from dataclasses import dataclass

from .step_limit_version_structure import StepLimitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StepLimit(StepLimitVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
