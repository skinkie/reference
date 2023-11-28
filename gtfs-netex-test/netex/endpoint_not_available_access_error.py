from dataclasses import dataclass
from netex.endpoint_not_available_access_structure import EndpointNotAvailableAccessStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class EndpointNotAvailableAccessError(EndpointNotAvailableAccessStructure):
    """Error:Recipient of a message to be distributed is not available.

    +SIRI v2.0
    """
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
