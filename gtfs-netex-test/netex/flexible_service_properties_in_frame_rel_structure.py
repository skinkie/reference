from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_service_properties import FlexibleServiceProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleServicePropertiesInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleServicePropertiesInFrame_RelStructure"

    flexible_service_properties: list[FlexibleServiceProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleServiceProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
