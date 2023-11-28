from dataclasses import dataclass
from netex.point_of_interest_space_ref_structure import PointOfInterestSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestSpaceRef(PointOfInterestSpaceRefStructure):
    """
    Reference to a POINT OF INTEREST SPACE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
