from dataclasses import dataclass

from .point_of_interest_classification_ref_structure import PointOfInterestClassificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestClassificationRef(PointOfInterestClassificationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
