from dataclasses import dataclass
from .service_access_code_ref_structure import ServiceAccessCodeRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceAccessCodeRef(ServiceAccessCodeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
