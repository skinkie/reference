from dataclasses import dataclass

from .site_path_junction_ref_structure import SitePathJunctionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathJunctionRef(SitePathJunctionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
