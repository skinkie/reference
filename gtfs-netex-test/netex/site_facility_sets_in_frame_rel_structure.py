from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.site_facility_set import SiteFacilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteFacilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE FACILITY SETs.
    """
    class Meta:
        name = "siteFacilitySetsInFrame_RelStructure"

    site_facility_set: List[SiteFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "SiteFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
