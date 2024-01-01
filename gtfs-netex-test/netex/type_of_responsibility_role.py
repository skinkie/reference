from dataclasses import dataclass
from .type_of_responsibility_role_value_structure import (
    TypeOfResponsibilityRoleValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfResponsibilityRole(TypeOfResponsibilityRoleValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
