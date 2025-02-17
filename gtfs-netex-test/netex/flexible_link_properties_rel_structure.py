from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .flexible_link_properties import FlexibleLinkProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FlexibleLinkPropertiesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "flexibleLinkProperties_RelStructure"

    flexible_link_properties: list[FlexibleLinkProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLinkProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
