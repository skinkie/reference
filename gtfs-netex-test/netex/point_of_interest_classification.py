from dataclasses import dataclass

from .point_of_interest_classification_version_structure import PointOfInterestClassificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestClassification(PointOfInterestClassificationVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
