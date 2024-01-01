from dataclasses import dataclass
from .unknown_extensions_error_structure import UnknownExtensionsErrorStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class UnknownExtensionsError(UnknownExtensionsErrorStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
