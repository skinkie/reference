from dataclasses import dataclass
from .service_facility_set_version_structure import (
    ServiceFacilitySetVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceFacilitySet(ServiceFacilitySetVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
