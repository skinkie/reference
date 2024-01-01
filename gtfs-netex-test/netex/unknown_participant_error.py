from dataclasses import dataclass
from .unknown_participant_error_structure import (
    UnknownParticipantErrorStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownParticipantError(UnknownParticipantErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
