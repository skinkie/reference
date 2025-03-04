from dataclasses import dataclass

from .contextualised_request_structure import ContextualisedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class ServiceRequestStructure(ContextualisedRequestStructure):
    pass
