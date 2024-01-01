from dataclasses import dataclass
from .invalid_data_references_error_structure import (
    InvalidDataReferencesErrorStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class InvalidDataReferencesError(InvalidDataReferencesErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
