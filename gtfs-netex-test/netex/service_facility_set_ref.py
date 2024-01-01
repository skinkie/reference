from dataclasses import dataclass
from .service_facility_set_ref_structure import ServiceFacilitySetRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySetRef(ServiceFacilitySetRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
