from dataclasses import dataclass
from netex.service_link_ref_structure import ServiceLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkRef(ServiceLinkRefStructure):
    """
    Reference to a SERVICE LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
