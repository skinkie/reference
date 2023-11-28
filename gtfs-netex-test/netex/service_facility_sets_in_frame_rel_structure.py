from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.service_facility_set import ServiceFacilitySet

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFacilitySetsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of SERVICE FACILITY SETs.
    """
    class Meta:
        name = "serviceFacilitySetsInFrame_RelStructure"

    service_facility_set: List[ServiceFacilitySet] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
