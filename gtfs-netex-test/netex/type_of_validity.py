from dataclasses import dataclass

from .type_of_validity_value_structure import TypeOfValidityValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfValidity(TypeOfValidityValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
