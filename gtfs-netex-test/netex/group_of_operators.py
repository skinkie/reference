from dataclasses import dataclass, field
from netex.group_of_operators_structure import GroupOfOperatorsStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfOperators(GroupOfOperatorsStructure):
    """
    A grouping of OPERATORs.

    :ivar id: Identifier of  GROUP OF OPERATORs.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
