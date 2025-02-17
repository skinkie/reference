from dataclasses import dataclass

from .service_capabilities_request_structure import ServiceCapabilitiesRequestStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataObjectCapabilitiesRequest(ServiceCapabilitiesRequestStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
