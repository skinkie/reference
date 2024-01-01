from dataclasses import dataclass
from .type_of_service_structure import TypeOfServiceStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfService(TypeOfServiceStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
