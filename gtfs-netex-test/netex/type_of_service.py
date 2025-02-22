from dataclasses import dataclass

from .type_of_service_structure import TypeOfServiceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfService(TypeOfServiceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
