from dataclasses import dataclass

from .response_structure import ResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractResponse(ResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
