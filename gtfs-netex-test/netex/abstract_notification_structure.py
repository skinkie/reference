from dataclasses import dataclass
from netex.producer_request_endpoint_structure import ProducerRequestEndpointStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractNotificationStructure(ProducerRequestEndpointStructure):
    """
    Type for Notification Request.
    """
