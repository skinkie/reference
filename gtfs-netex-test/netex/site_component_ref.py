from dataclasses import dataclass

from .site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteComponentRef(SiteComponentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
