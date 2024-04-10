from dataclasses import dataclass

from .type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEntityRef(TypeOfValueRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
