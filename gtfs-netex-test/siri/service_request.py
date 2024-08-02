from dataclasses import dataclass

from .service_request_structure import ServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ServiceRequest(ServiceRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
