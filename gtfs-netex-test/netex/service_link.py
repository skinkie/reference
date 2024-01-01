from dataclasses import dataclass
from .service_link_version_structure import ServiceLinkVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLink(ServiceLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
