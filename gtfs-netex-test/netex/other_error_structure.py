from dataclasses import dataclass

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class OtherErrorStructure(ErrorCodeStructure):
    pass
