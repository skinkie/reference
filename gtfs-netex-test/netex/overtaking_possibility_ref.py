from dataclasses import dataclass
from netex.overtaking_possibility_ref_structure import OvertakingPossibilityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OvertakingPossibilityRef(OvertakingPossibilityRefStructure):
    """
    Reference to an  OVERTAKING POSSIBILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
