from dataclasses import dataclass

from .abstract_service_request_structure import AbstractServiceRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class AbstractServiceRequest(AbstractServiceRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
