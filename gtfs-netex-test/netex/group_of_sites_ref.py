from dataclasses import dataclass

from .group_of_sites_ref_structure import GroupOfSitesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSitesRef(GroupOfSitesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
