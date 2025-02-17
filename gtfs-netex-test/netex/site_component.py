from dataclasses import dataclass

from .site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SiteComponent(SiteComponentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
