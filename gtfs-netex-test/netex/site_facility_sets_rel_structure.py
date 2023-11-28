from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.site_facility_set import SiteFacilitySet
from netex.site_facility_set_ref import SiteFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SiteFacilitySetsRelStructure(ContainmentAggregationStructure):
    """
    SITE FACILITies associated with entity.
    """
    class Meta:
        name = "siteFacilitySets_RelStructure"

    site_facility_set_ref_or_site_facility_set: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySet",
                    "type": SiteFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
