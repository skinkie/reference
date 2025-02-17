from dataclasses import dataclass

from .type_of_validity_ref_structure import TypeOfValidityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfValidityRef(TypeOfValidityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
