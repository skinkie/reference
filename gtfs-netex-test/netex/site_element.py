from dataclasses import dataclass

from .site_element_version_structure import SiteElementVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteElement(SiteElementVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
