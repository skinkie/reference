from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.point_of_interest_classification import PointOfInterestClassification

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestClassificationsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of POINT OF INTEREST CLASSIFICATION.
    """
    class Meta:
        name = "pointOfInterestClassificationsInFrame_RelStructure"

    point_of_interest_classification: List[PointOfInterestClassification] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassification",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
