from dataclasses import dataclass

from .site_element_ref_structure import SiteElementRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteElementRef(SiteElementRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
