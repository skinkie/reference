from dataclasses import dataclass

from .status_response_structure import StatusResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class ResponseStatus(StatusResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
