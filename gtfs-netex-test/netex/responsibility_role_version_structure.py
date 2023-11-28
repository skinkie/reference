from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.type_of_responsibility_role_ref import TypeOfResponsibilityRoleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilityRoleVersionStructure(DataManagedObjectStructure):
    """Type for a  RESPONSIBILITY ROLE  that can be associated with a DATA MANAGED
    OBJECT.

    A Child ENTITY has the same responsibilities as its parent.

    :ivar name: Explanation of RESPONSIBILITY ROLE.
    :ivar description: Explanation of REsponsibility RoleSET.
    :ivar type_of_responsibility_role_ref:
    """
    class Meta:
        name = "ResponsibilityRole_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_responsibility_role_ref: Optional[TypeOfResponsibilityRoleRef] = field(
        default=None,
        metadata={
            "name": "TypeOfResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
