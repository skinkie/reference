from dataclasses import dataclass
from netex.network_restriction_ref_structure import NetworkRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OvertakingPossibilityRefStructure(NetworkRestrictionRefStructure):
    """
    Type for Reference to  an  OVERTAKING POSSIBILITY.
    """
