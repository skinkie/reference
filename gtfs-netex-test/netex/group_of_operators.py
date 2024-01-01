from dataclasses import dataclass
from .group_of_operators_structure import GroupOfOperatorsStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfOperators(GroupOfOperatorsStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
