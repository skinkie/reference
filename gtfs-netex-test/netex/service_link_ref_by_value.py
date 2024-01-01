from dataclasses import dataclass
from .service_link_ref_by_value_structure import ServiceLinkRefByValueStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkRefByValue(ServiceLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
