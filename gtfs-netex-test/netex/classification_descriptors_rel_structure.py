from dataclasses import dataclass, field
from typing import List
from netex.classification_descriptor_version_structure import ClassificationDescriptorVersionStructure
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClassificationDescriptorsRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of POINT OF INTEREST CLASSIFICATION DESCRIPTORs.

    :ivar classification_descriptor: Alternative descriptor for a POINT
        OF INTEREST Classification.
    """
    class Meta:
        name = "classificationDescriptors_RelStructure"

    classification_descriptor: List[ClassificationDescriptorVersionStructure] = field(
        default_factory=list,
        metadata={
            "name": "ClassificationDescriptor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
