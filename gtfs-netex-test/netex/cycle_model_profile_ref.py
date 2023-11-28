from dataclasses import dataclass
from netex.cycle_model_profile_ref_structure import CycleModelProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CycleModelProfileRef(CycleModelProfileRefStructure):
    """Reference to a CYCLE MODEL PROFILE.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
