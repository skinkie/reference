from dataclasses import dataclass
from netex.point_of_interest_classification_ref_structure import PointOfInterestClassificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationRef(PointOfInterestClassificationRefStructure):
    """
    Classification of a POINT OF INTEREST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
