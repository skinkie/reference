from dataclasses import dataclass

from .restricted_service_facility_set_version_structure import RestrictedServiceFacilitySetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RestrictedServiceFacilitySet(RestrictedServiceFacilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
