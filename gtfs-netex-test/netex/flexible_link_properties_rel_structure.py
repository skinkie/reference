from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.flexible_link_properties import FlexibleLinkProperties

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleLinkPropertiesRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of FLEXIBLE LINK PROPERTies.
    """
    class Meta:
        name = "flexibleLinkProperties_RelStructure"

    flexible_link_properties: List[FlexibleLinkProperties] = field(
        default_factory=list,
        metadata={
            "name": "FlexibleLinkProperties",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
