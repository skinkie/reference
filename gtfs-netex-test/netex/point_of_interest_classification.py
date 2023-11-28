from dataclasses import dataclass, field
from netex.point_of_interest_classification_version_structure import PointOfInterestClassificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassification(PointOfInterestClassificationVersionStructure):
    """
    Classification of a POINT OF INTEREST.

    :ivar id: Identifier of a POINT OF INTEREST CLASSIFICATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
