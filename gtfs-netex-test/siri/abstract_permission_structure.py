from dataclasses import dataclass, field
from typing import Optional, Union

from .empty_type import EmptyType
from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractPermissionStructure:
    all_participants_or_participant_ref: Optional[Union[EmptyType, ParticipantRefStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllParticipants",
                    "type": EmptyType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ParticipantRef",
                    "type": ParticipantRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    general_capabilities: Optional["AbstractPermissionStructure.GeneralCapabilities"] = field(
        default=None,
        metadata={
            "name": "GeneralCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class GeneralCapabilities:
        request_response: bool = field(
            default=True,
            metadata={
                "name": "RequestResponse",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
        publish_subscribe: bool = field(
            default=True,
            metadata={
                "name": "PublishSubscribe",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "required": True,
            },
        )
