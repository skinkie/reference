from dataclasses import dataclass

from .participant_ref_structure import ParticipantRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class RequestorRef(ParticipantRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
