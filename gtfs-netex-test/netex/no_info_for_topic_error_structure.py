from dataclasses import dataclass
from .error_code_structure import ErrorCodeStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class NoInfoForTopicErrorStructure(ErrorCodeStructure):
    pass
