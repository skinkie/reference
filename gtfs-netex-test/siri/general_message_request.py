from dataclasses import dataclass

from .general_message_request_structure import GeneralMessageRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class GeneralMessageRequest(GeneralMessageRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
