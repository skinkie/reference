from dataclasses import dataclass, field
from typing import Union

from .complex_feature import ComplexFeature
from .containment_aggregation_structure import ContainmentAggregationStructure
from .simple_feature import SimpleFeature

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SpatialFeaturesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "spatialFeaturesInFrame_RelStructure"

    simple_feature_or_complex_feature: list[Union[SimpleFeature, ComplexFeature]] = field(
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
        },
    )
