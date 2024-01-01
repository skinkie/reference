from dataclasses import dataclass
from .group_of_lines_ref_structure import GroupOfLinesRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinesRef(GroupOfLinesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
