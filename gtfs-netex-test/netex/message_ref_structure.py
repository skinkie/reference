from dataclasses import dataclass

from .message_qualifier_structure import MessageQualifierStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class MessageRefStructure(MessageQualifierStructure):
    pass
