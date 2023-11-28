from dataclasses import dataclass, field
from netex.type_of_responsibility_role_value_structure import TypeOfResponsibilityRoleValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfResponsibilityRole(TypeOfResponsibilityRoleValueStructure):
    """
    Classification of a RESPONSIBILITY ROLE.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
