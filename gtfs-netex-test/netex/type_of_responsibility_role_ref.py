from dataclasses import dataclass

from .type_of_responsibility_role_ref_structure import TypeOfResponsibilityRoleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfResponsibilityRoleRef(TypeOfResponsibilityRoleRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
