from dataclasses import dataclass
from netex.responsibility_role_ref_structure import ResponsibilityRoleRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ResponsibilityRoleRef(ResponsibilityRoleRefStructure):
    """
    Reference to a RESPONSIBILITY ROLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
