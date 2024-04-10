from dataclasses import dataclass

from .group_of_links_version_structure import GroupOfLinksVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinks(GroupOfLinksVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
