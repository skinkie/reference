from dataclasses import dataclass

from .type_of_activation_value_structure import TypeOfActivationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfActivation(TypeOfActivationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
