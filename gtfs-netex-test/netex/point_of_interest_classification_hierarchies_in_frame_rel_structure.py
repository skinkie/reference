from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .point_of_interest_classification_hierarchy import PointOfInterestClassificationHierarchy

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestClassificationHierarchiesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "pointOfInterestClassificationHierarchiesInFrame_RelStructure"

    point_of_interest_classification_hierarchy: list[PointOfInterestClassificationHierarchy] = field(
        default_factory=list,
        metadata={
            "name": "PointOfInterestClassificationHierarchy",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
