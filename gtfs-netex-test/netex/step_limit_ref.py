from dataclasses import dataclass
from netex.step_limit_ref_structure import StepLimitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class StepLimitRef(StepLimitRefStructure):
    """
    Reference to a STEP LIMIT PARAMETER.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
