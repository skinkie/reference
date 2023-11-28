from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.service_facility_set import ServiceFacilitySet
from netex.service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceFacilitySetsRelStructure(ContainmentAggregationStructure):
    """
    SERVICE FACILITY SETs associated with entity.
    """
    class Meta:
        name = "serviceFacilitySets_RelStructure"

    service_facility_set_ref_or_service_facility_set: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFacilitySet",
                    "type": ServiceFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
