from dataclasses import dataclass
from netex.capabilities_response_structure import CapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class CapabilitiesResponse(CapabilitiesResponseStructure):
    """
    Responses with the capabilities of an implementation.
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
