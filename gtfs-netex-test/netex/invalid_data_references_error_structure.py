from dataclasses import dataclass, field

from .error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InvalidDataReferencesErrorStructure(ErrorCodeStructure):
    invalid_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "InvalidRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
