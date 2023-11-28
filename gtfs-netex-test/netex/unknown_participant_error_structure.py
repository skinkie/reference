from dataclasses import dataclass, field
from typing import Optional
from netex.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class UnknownParticipantErrorStructure(ErrorCodeStructure):
    """Type for Error: Unknown Participant. +SIRI v2.0

    :ivar participant_ref: Reference to  Participant who is unknown. +
        SIRI v2.0
    """
    participant_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
