from dataclasses import dataclass
from netex.contextualised_request_structure import ContextualisedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ServiceRequestStructure(ContextualisedRequestStructure):
    """
    SIRI Service Request.
    """
