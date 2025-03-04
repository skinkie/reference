from dataclasses import dataclass

from .service_access_code_version_structure import ServiceAccessCodeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceAccessCode(ServiceAccessCodeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
