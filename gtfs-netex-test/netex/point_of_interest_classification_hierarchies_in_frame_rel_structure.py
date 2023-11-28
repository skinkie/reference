from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_of_interest_classification_hierarchy import PointOfInterestClassificationHierarchy

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationHierarchiesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of POINT OF INTEREST CLASSIFICATION Hierarchy.
    """
    class Meta:
        name = "pointOfInterestClassificationHierarchiesInFrame_RelStructure"

    point_of_interest_classification_hierarchy: List[PointOfInterestClassificationHierarchy] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationHierarchy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
