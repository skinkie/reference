from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .restricted_service_facility_set_ref import RestrictedServiceFacilitySetRef
from .service_facility_set import ServiceFacilitySet
from .service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "serviceFacilitySets_RelStructure"

    restricted_service_facility_set_ref_or_service_facility_set_ref_or_service_facility_set: List[Union[RestrictedServiceFacilitySetRef, ServiceFacilitySetRef, ServiceFacilitySet]] = field(
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
        },
    )
