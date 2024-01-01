from dataclasses import dataclass
from .status_response_structure import StatusResponseStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ResponseStatus(StatusResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
