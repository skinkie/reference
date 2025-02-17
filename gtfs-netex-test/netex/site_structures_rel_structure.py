from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .site_structure import SiteStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteStructuresRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "siteStructures_RelStructure"

    site_structure: list[SiteStructure] = field(
        default_factory=list,
        metadata={
            "name": "SiteStructure",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
