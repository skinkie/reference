from dataclasses import dataclass

from .extensions_structure import ExtensionsStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class Extensions1(ExtensionsStructure):
    class Meta:
        name = "Extensions"
        namespace = "http://www.siri.org.uk/siri"
