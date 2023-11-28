from dataclasses import dataclass, field
from typing import List
from netex.error_code_structure import ErrorCodeStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class InvalidDataReferencesErrorStructure(ErrorCodeStructure):
    """Type for InvalidDataReferencesError:.

    +SIRI v2.0.

    :ivar invalid_ref: Invalid reference values encoountered.
    """
    invalid_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "InvalidRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
