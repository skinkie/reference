from dataclasses import dataclass, field
from typing import List
from netex.complex_feature import ComplexFeature
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.simple_feature import SimpleFeature

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SpatialFeaturesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of TSPATIAL FEATURe.
    """
    class Meta:
        name = "spatialFeaturesInFrame_RelStructure"

    simple_feature_or_complex_feature: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleFeature",
                    "type": SimpleFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplexFeature",
                    "type": ComplexFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
