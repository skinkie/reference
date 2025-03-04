from dataclasses import dataclass

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class AbstractFunctionalServiceCapabilitiesResponse(AbstractServiceCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
