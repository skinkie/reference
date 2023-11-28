from dataclasses import dataclass
from netex.point_of_interest_derived_view_structure import PointOfInterestDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestView(PointOfInterestDerivedViewStructure):
    """
    Simplified view of POINT OF INTEREST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
