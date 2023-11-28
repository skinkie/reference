from dataclasses import dataclass
from netex.rounding_step_ref_structure import RoundingStepRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundingStepRef(RoundingStepRefStructure):
    """
    Reference to a ROUNDING STEP.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
