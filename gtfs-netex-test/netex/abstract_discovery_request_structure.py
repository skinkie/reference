from dataclasses import dataclass, field
from typing import Optional
from netex.authenticated_request_structure import AuthenticatedRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class AbstractDiscoveryRequestStructure(AuthenticatedRequestStructure):
    """
    Requests for stop reference data for use in service requests.

    :ivar address: Address to which response is to be sent. This may
        also be determined from RequestorRef and preconfigured data.
    :ivar requestor_ref:
    :ivar message_identifier: Arbitrary unique identifier that can be
        used to reference this message in subsequent interactions.
    """
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    requestor_ref: str = field(
        metadata={
            "name": "RequestorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    message_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "MessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
