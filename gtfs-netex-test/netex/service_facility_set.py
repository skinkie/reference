from dataclasses import dataclass

from .service_facility_set_version_structure import ServiceFacilitySetVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceFacilitySet(ServiceFacilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
