from dataclasses import dataclass, field
from typing import List

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InvalidDataReferencesErrorStructure(ErrorCodeStructure):
    invalid_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InvalidRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
