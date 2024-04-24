from dataclasses import dataclass

from .group_of_sites_version_structure import GroupOfSitesVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSites(GroupOfSitesVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
