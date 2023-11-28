from dataclasses import dataclass, field
from typing import Optional
from netex.classification_descriptors_rel_structure import ClassificationDescriptorsRelStructure
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationVersionStructure(TypeOfValueVersionStructure):
    """
    Type for Classification of a POINT OF INTEREST.

    :ivar alternative_descriptors: Alternative descriptors.
    """
    class Meta:
        name = "PointOfInterestClassification_VersionStructure"

    alternative_descriptors: Optional[ClassificationDescriptorsRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeDescriptors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
