from dataclasses import dataclass

from .restricted_service_facility_set_ref_structure import RestrictedServiceFacilitySetRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RestrictedServiceFacilitySetRef(RestrictedServiceFacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
