from dataclasses import dataclass

from .site_structure_ref_structure import SiteStructureRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteStructureRef(SiteStructureRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
