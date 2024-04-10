from dataclasses import dataclass

from .site_entrance_version_structure import SiteEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Entrance(SiteEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
