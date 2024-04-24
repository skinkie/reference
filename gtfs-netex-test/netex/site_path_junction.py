from dataclasses import dataclass

from .site_path_junction_version_structure import SitePathJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SitePathJunction(SitePathJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
