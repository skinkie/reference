from dataclasses import dataclass
from .extensions_structure_1 import ExtensionsStructure1


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Extensions1(ExtensionsStructure1):
    class Meta:
        name = "Extensions"
        namespace = "http://www.siri.org.uk/siri"
