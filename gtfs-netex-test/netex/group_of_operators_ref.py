from dataclasses import dataclass

from .group_of_operators_ref_structure import GroupOfOperatorsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfOperatorsRef(GroupOfOperatorsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
