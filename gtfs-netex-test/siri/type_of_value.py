from dataclasses import dataclass

from .type_of_value_structure import TypeOfValueStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TypeOfValue(TypeOfValueStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
