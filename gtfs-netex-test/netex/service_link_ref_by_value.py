from dataclasses import dataclass
from netex.service_link_ref_by_value_structure import ServiceLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceLinkRefByValue(ServiceLinkRefByValueStructure):
    """
    Reference to a SERVICE LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
