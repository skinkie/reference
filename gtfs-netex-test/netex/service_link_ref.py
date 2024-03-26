from dataclasses import dataclass

from .service_link_ref_structure import ServiceLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkRef(ServiceLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
