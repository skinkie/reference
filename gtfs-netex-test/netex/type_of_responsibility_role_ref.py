from dataclasses import dataclass
from netex.type_of_responsibility_role_ref_structure import TypeOfResponsibilityRoleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfResponsibilityRoleRef(TypeOfResponsibilityRoleRefStructure):
    """
    Reference to an TYPE OF RESPONSIBILITY ROLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
