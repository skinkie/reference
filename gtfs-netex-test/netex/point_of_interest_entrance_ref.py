from dataclasses import dataclass
from netex.point_of_interest_entrance_ref_structure import PointOfInterestEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestEntranceRef(PointOfInterestEntranceRefStructure):
    """
    Reference to a POINT OF INTEREST ENTRANCE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
