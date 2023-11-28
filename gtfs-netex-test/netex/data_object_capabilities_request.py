from dataclasses import dataclass
from netex.service_capabilities_request_structure import ServiceCapabilitiesRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    """Request for information about DATA OBJECT Service Capabilities.

    Answered with DataObjectCapabilitiesResponse.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
