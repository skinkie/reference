from dataclasses import dataclass

from .site_structure_version_structure import SiteStructureVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteStructure(SiteStructureVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
