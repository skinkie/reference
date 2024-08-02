from dataclasses import dataclass

from .types_of_value_structure import TypesOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TypesOfValue(TypesOfValueStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
