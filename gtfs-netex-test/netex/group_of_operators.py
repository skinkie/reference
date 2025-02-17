from dataclasses import dataclass

from .group_of_operators_structure import GroupOfOperatorsStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfOperators(GroupOfOperatorsStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
