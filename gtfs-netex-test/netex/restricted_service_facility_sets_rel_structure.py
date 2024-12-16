from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .restricted_service_facility_set import RestrictedServiceFacilitySet
from .restricted_service_facility_set_ref import RestrictedServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedServiceFacilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "restrictedServiceFacilitySets_RelStructure"

    restricted_service_facility_set_ref_or_restricted_service_facility_set: List[Union[RestrictedServiceFacilitySetRef, RestrictedServiceFacilitySet]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RestrictedServiceFacilitySetRef",
                    "type": RestrictedServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedServiceFacilitySet",
                    "type": RestrictedServiceFacilitySet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
