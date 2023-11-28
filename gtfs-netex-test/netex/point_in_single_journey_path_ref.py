from dataclasses import dataclass
from netex.point_in_single_journey_path_ref_structure import PointInSingleJourneyPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointInSingleJourneyPathRef(PointInSingleJourneyPathRefStructure):
    """Reference to a POINT IN SINGLE JOURNEY PATH.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
