from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .site_facility_set import SiteFacilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteFacilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "siteFacilitySetsInFrame_RelStructure"

    site_facility_set: list[SiteFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "SiteFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
