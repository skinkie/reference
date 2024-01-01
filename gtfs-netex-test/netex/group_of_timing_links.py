from dataclasses import dataclass
from .group_of_timing_links_rel_structure import GroupOfTimingLinksRelStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimingLinks(GroupOfTimingLinksRelStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
