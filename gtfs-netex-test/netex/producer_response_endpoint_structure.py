from dataclasses import dataclass, field
from typing import Optional

from .message_qualifier_structure import MessageQualifierStructure
from .message_ref_structure import MessageRefStructure
from .participant_ref_structure import ParticipantRefStructure
from .response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class ProducerResponseEndpointStructure(ResponseStructure):
    producer_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ProducerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    address: Optional[str] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    response_message_identifier: Optional[MessageQualifierStructure] = field(
        default=None,
        metadata={
            "name": "ResponseMessageIdentifier",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    request_message_ref: Optional[MessageRefStructure] = field(
        default=None,
        metadata={
            "name": "RequestMessageRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
