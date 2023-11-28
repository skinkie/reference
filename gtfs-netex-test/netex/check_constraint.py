from dataclasses import dataclass, field
from netex.check_constraint_version_structure import CheckConstraintVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraint(CheckConstraintVersionStructure):
    """Characteristics of a SITE COMPONENT representing a process, such as check-
    in, security screening, ticket control or immigration, that may potentially
    incur a time penalty that should be allowed for when journey planning.

    Used to mark PATH LINKs to determine transit routes through
    interchanges.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
