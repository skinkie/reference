from dataclasses import dataclass

from .service_link_ref_by_value_structure import ServiceLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ServiceLinkRefByValue(ServiceLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
